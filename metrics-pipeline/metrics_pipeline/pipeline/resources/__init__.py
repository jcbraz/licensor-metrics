import os
from dagster import EnvVar
from dagster_gcp import BigQueryResource
from upstash_redis import Redis

bigquery_resource = BigQueryResource(
    project="licensor-metrics", gcp_credentials=EnvVar("GOOGLE_CLOUD_API_KEY")
)

redis_resource = Redis(
    url=os.environ["UPSTASH_REDIS_URI"], token=os.environ["UPSTASH_REDIS_TOKEN"]
)
