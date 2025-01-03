import pandas as pd
from uuid import uuid4
from loguru import logger
from dagster import asset, MaterializeResult
from dagster_gcp import BigQueryResource, BigQueryError

from .constants import LATEST_PROCESSED_TIME_PATH, BATCH_ID_PATH


@asset(group_name="extract")
def latest_process_time(bigquery: BigQueryResource) -> MaterializeResult:
    query = """
        SELECT
            MAX(processed_time) AS latest_processed_time
        FROM `user_activity.plays`
    """

    with bigquery.get_client() as client:
        try:
            processed_time_df: pd.DataFrame = client.query(query=query).to_dataframe()
            if processed_time_df.empty:
                df_to_write = pd.DataFrame(data=[{"latest_processed_time": 0}])
                df_to_write.to_csv(LATEST_PROCESSED_TIME_PATH)
            else:
                processed_time_df["latest_processed_time"].to_csv(
                    LATEST_PROCESSED_TIME_PATH
                )

            return MaterializeResult(
                metadata={
                    "Latest Processed Timestamp": str(
                        processed_time_df["latest_processed_time"][0]
                    )
                }
            )
        except (BigQueryError, pd.errors.DataError) as e:
            logger.error(e)


@asset(group_name="load")
def generate_batch_id() -> None:
    try:
        recent_batch_id = str(uuid4())
        with open(file=BATCH_ID_PATH, mode="w", encoding="utf-8") as file:
            file.write(recent_batch_id)
    except Exception as e:
        logger.error(e)
