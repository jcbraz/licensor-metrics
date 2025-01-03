import os
import typing
import pandas as pd
from dagster import asset, MaterializeResult
from loguru import logger
from dagster_gcp import BigQueryResource, BigQueryError
from upstash_redis.errors import UpstashError
from ..resources import redis_resource
from .dbt import licensor_metrics_dbt_assets


def get_metrics(
    bigquery: BigQueryResource, table_name: str
) -> typing.Union[pd.DataFrame, None]:
    try:
        sql: str = f"SELECT * FROM `user_activity.{table_name}`"
        df: pd.DataFrame = pd.DataFrame()

        with bigquery.get_client() as bqclient:
            df: pd.DataFrame = bqclient.query(query=sql).result().to_dataframe()

        if df.empty:
            raise pd.errors.DataError(f"DataFrame for {table_name} turned out empty!")

        return df
    except BigQueryError as e:
        logger.error(e)
        return None


@asset(deps=[licensor_metrics_dbt_assets], group_name="serve")
def redis_cache(bigquery: BigQueryResource) -> MaterializeResult:

    marts_tables = [
        "mart_country_market_share",
        "mart_top_track",
        "mart_top_track_per_country",
        "mart_total_hours_played",
    ]

    successful_insertions: list[str] = []

    for table in marts_tables:
        try:
            incoming_df = get_metrics(bigquery=bigquery, table_name=table)

            df_json = incoming_df.to_json()
            insertion_result = redis_resource.set(key=table, value=df_json)
            if not insertion_result:
                raise UpstashError(f"Error inserting value {table} into the cache.")

            successful_insertions.append(table)
        except UpstashError as e:
            logger.error(e)
            return MaterializeResult(
                metadata={
                    "Status": f"Error in {table}",
                    "Successful Insertions": ",".join(successful_insertions),
                }
            )

    return MaterializeResult(metadata={"Status": "Success"})
