from dagster import EnvVar
from dagster_gcp import BigQueryResource

bigquery_resource = BigQueryResource(
    project="licensor-metrics",
    gcp_credentials=EnvVar("GOOGLE_CLOUD_API_KEY")
)