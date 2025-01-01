import os
import logging
import polars as pl
from typing import Tuple
from dagster_gcp import BigQueryResource, BigQueryError
from dagster import asset, MaterializeResult
from loguru import logger


from .constants import (
    BATCH_ID_PATH,
    PLAYS_FILE_PATH,
    LOCATIONS_FILE_PATH,
    TRACKS_FILE_PATH,
)
from .common import generate_batch_id
from .postgres import play_table, location_table, track_table


def get_batch_id() -> str:
    try:
        with open(file=BATCH_ID_PATH, mode="r", encoding="utf-8") as file:
            batch_id = str(file.read().strip())

        return batch_id
    except FileExistsError as e:
        logger.error(e)


def batch_split_lazy(
    lazy_df: pl.LazyFrame, batch_size: int = 10000
) -> Tuple[list[pl.LazyFrame], int]:
    """Split polars lazy dataframe into batches for processing.

    Args:
        df (pl.LazyFrame): LazyFrame to split
        batch_size (int, optional): Size of each batch. Defaults to 10000.

    Returns:
        list[pl.LazyFrame]: List of lazy dataframe batches
    """
    total_rows: int = lazy_df.select(pl.len()).collect().item()
    num_batches: int = (total_rows + batch_size - 1) // batch_size

    batches = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, total_rows)
        batch = (
            lazy_df.with_row_index()
            .filter((pl.col("index") >= start_idx) & (pl.col("index") < end_idx))
            .lazy()
        )
        batches.append(batch)

    return batches, total_rows


@asset(deps=[location_table, generate_batch_id], group_name="load")
def ingest_locations(bigquery: BigQueryResource) -> MaterializeResult:
    batch_id: str = ""
    try:
        batch_id = get_batch_id()
        if not batch_id:
            logger.warning("No batch ID found")
            return MaterializeResult(metadata={"Rows Processed": 0})
    except FileExistsError as e:
        logger.error(f"Error reading batch id: {e}")
        return MaterializeResult(metadata={"Rows Processed": 0})

    if not os.path.exists(LOCATIONS_FILE_PATH):
        logger.info(f"Locations file not found at {LOCATIONS_FILE_PATH}")
        return MaterializeResult(metadata={"Rows Processed": 0})

    try:
        incoming_locations_df: pl.LazyFrame = pl.scan_parquet(
            source=LOCATIONS_FILE_PATH
        ).with_columns(
            [
                pl.lit(str(batch_id)).alias("batch_id"),
                pl.col("processed_time").str.strptime(
                    pl.Datetime, format="%Y-%m-%d %H:%M:%S"
                ),
            ]
        )

        if incoming_locations_df.limit(1).collect().is_empty():
            logger.info("Locations file is empty")
            return MaterializeResult(metadata={"Rows Processed": 0})

        total_rows: int = incoming_locations_df.select(pl.len()).collect().item()

        try:
            with bigquery.get_client() as client:
                clean_incoming_locations_df = (
                    incoming_locations_df.collect()
                    .to_pandas()
                    .drop(columns=["index"], errors="ignore")
                )
                location_job = client.load_table_from_dataframe(
                    dataframe=clean_incoming_locations_df,
                    destination="user_activity.locations",
                )
                location_job.result()

            logger.info(f"Successfully processed {total_rows} rows")

            os.remove(path=LOCATIONS_FILE_PATH)
            return MaterializeResult(metadata={"Rows Processed": total_rows})

        except BigQueryError as e:
            logger.error(f"BigQuery error: {e}")
            return MaterializeResult(metadata={"Rows Processed": 0, "Error": str(e)})

    except pl.exceptions.NoDataError as e:
        logger.error(f"Polars error: {e}")
        return MaterializeResult(metadata={"Rows Processed": 0})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return MaterializeResult(metadata={"Rows Processed": 0})


@asset(deps=[track_table, generate_batch_id], group_name="load")
def ingest_tracks(bigquery: BigQueryResource) -> MaterializeResult:
    batch_id: str = ""
    try:
        batch_id = get_batch_id()
        if not batch_id:
            raise FileExistsError("Error reading batch id file!")
    except FileExistsError as e:
        logger.error(e)
        return MaterializeResult(metadata={"Rows Processed": 0})

    if not os.path.exists(TRACKS_FILE_PATH):
        logger.info(f"Tracks file not found at {TRACKS_FILE_PATH}")
        return MaterializeResult(metadata={"Rows Processed": 0})

    try:
        incoming_tracks_df: pl.LazyFrame = pl.scan_parquet(
            source=TRACKS_FILE_PATH
        ).with_columns(
            [
                pl.lit(str(batch_id)).alias("batch_id"),
                pl.col("processed_time").str.strptime(
                    pl.Datetime, format="%Y-%m-%d %H:%M:%S"
                ),
            ]
        )

        if incoming_tracks_df.limit(1).collect().is_empty():
            logger.info("Incoming tracks file turned out empty!")
            return MaterializeResult(metadata={"Rows Processed": 0})

        (incoming_plays_batches, total_rows) = batch_split_lazy(
            lazy_df=incoming_tracks_df
        )

        for i, batch in enumerate(incoming_plays_batches):
            try:
                with bigquery.get_client() as client:
                    collected_batch_df = (
                        batch.collect()
                        .to_pandas()
                        .drop(columns=["index"], errors="ignore")
                    )
                    play_batch_job = client.load_table_from_dataframe(
                        dataframe=collected_batch_df,
                        destination="user_activity.tracks",
                    )
                    play_batch_job.result()
            except BigQueryError as e:
                logging.error(e)
                return MaterializeResult(
                    metadata={
                        "Batch Number Failure": i,
                        "Number of Rows Inserted Into Tracks": 10000 * i,
                    }
                )

        os.remove(path=TRACKS_FILE_PATH)

        return MaterializeResult(metadata={"Rows Inserted Into plays": total_rows})

    except FileNotFoundError as e:
        logger.error(e)
        return MaterializeResult(metadata={"Rows processed": 0})


@asset(deps=[play_table, generate_batch_id], group_name="load")
def ingest_plays(bigquery: BigQueryResource) -> MaterializeResult:

    batch_id: str = ""
    try:
        batch_id = get_batch_id()
        if not batch_id:
            raise FileExistsError("Error reading batch id file!")
    except FileExistsError as e:
        logger.error(e)

    if not os.path.exists(PLAYS_FILE_PATH):
        logger.info(f"Plays file not found at {PLAYS_FILE_PATH}")
        return MaterializeResult(metadata={"Rows Processed": 0})

    incoming_plays_df: pl.LazyFrame = (
        pl.scan_parquet(source=PLAYS_FILE_PATH)
        .with_columns([pl.lit(str(batch_id)).alias("batch_id")])
        .rename(
            {
                "locationid": "location_id",
                "trackid": "track_id",
                "playedms": "played_ms",
            }
        )
    )

    if incoming_plays_df.limit(1).collect().is_empty():
        logger.info("Incoming tracks file turned out empty!")
        return MaterializeResult(metadata={"Rows Processed": 0})

    (incoming_plays_batches, total_rows) = batch_split_lazy(lazy_df=incoming_plays_df)

    for i, batch in enumerate(incoming_plays_batches):

        try:
            with bigquery.get_client() as client:
                collected_batch_df = (
                    batch.collect().to_pandas().drop(columns=["index"], errors="ignore")
                )
                play_batch_job = client.load_table_from_dataframe(
                    dataframe=collected_batch_df,
                    destination="user_activity.plays",
                )

                play_batch_job.result()

        except BigQueryError as e:
            logging.error(e)
            return MaterializeResult(
                metadata={
                    "Batch Number Failure": i,
                    "Number of Rows Inserted Into Plays": 10000 * i,
                }
            )

    os.remove(path=PLAYS_FILE_PATH)

    return MaterializeResult(metadata={"Rows Inserted Into plays": total_rows})
