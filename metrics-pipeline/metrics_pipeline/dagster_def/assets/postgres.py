import os
import polars as pl
from typing import Union
from dagster import asset, DagsterExecutionInterruptedError, MaterializeResult
from loguru import logger
from datetime import datetime
from .constants import (
    PLAYS_FILE_PATH,
    LOCATIONS_FILE_PATH,
    TRACKS_FILE_PATH,
    LATEST_PROCESSED_TIME_PATH,
)
from .common import latest_process_time


def get_latest_processed_time() -> Union[str, None]:
    latest_process_time_df = pl.read_csv(
        source=LATEST_PROCESSED_TIME_PATH, columns=["latest_processed_time"]
    )
    if latest_process_time_df.is_empty():
        return None

    latest_process_time = latest_process_time_df["latest_processed_time"][0]
    if latest_process_time == 0:
        return None

    if not isinstance(latest_process_time, str):
        latest_process_time = str(latest_process_time)

    dt = datetime.fromisoformat(latest_process_time)
    return f"'{dt.isoformat()}'"


@asset(deps=[latest_process_time], group_name="extract")
def location_table() -> MaterializeResult:

    latest_processed_time = get_latest_processed_time()

    query = (
        "SELECT * FROM location"
        if not latest_processed_time
        else f"SELECT * FROM location WHERE processed_time > {latest_processed_time}"
    )

    try:
        locations_df = pl.read_database_uri(query=query, uri=os.environ["POSTGRES_URI"])
        if locations_df.is_empty():
            return MaterializeResult(metadata={"Rows processed": 0})

        locations_df.write_parquet(file=LOCATIONS_FILE_PATH, compression="zstd")

        return MaterializeResult(
            metadata={"Rows processed": locations_df.select(pl.len()).item()}
        )

    except (DagsterExecutionInterruptedError, pl.exceptions.NoDataError) as e:
        logger.error(e)
        raise


@asset(deps=[latest_process_time], group_name="extract")
def track_table() -> None:

    latest_processed_time = get_latest_processed_time()
    query = (
        "SELECT * FROM track"
        if not latest_processed_time
        else f"SELECT * FROM track WHERE processed_time > {latest_processed_time}"
    )

    try:
        tracks_df = pl.read_database_uri(query=query, uri=os.environ["POSTGRES_URI"])
        if tracks_df.is_empty():
            return MaterializeResult(metadata={"Rows processed": 0})

        tracks_df.write_parquet(file=TRACKS_FILE_PATH, compression="zstd")

        return MaterializeResult(
            metadata={"Rows processed": tracks_df.select(pl.len()).item()}
        )

    except (DagsterExecutionInterruptedError, pl.exceptions.NoDataError) as e:
        logger.error(e)
        raise


@asset(deps=[latest_process_time, location_table, track_table], group_name="extract")
def play_table() -> None:

    latest_processed_time = get_latest_processed_time()
    query = (
        "SELECT * FROM play"
        if not latest_processed_time
        else f"SELECT * FROM play WHERE processed_time > {latest_processed_time}"
    )

    try:
        play_df = pl.read_database_uri(query=query, uri=os.environ["POSTGRES_URI"])
        if play_df.is_empty():
            return MaterializeResult(metadata={"Rows processed": 0})

        play_df.write_parquet(file=PLAYS_FILE_PATH, compression="zstd")

        return MaterializeResult(metadata={"Rows processed": play_df.select(pl.len()).item()})

    except (DagsterExecutionInterruptedError, pl.exceptions.NoDataError) as e:
        logger.error(e)
        raise
