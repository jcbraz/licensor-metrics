from dagster_dbt import DbtCliResource
from dagster import Definitions, load_assets_from_modules
from .assets.dbt import licensor_metrics_dbt_assets, licensor_metrics_project
from .assets import bigquery, common,  postgres
from .resources import bigquery_resource

common_assets = load_assets_from_modules([common])
postgres_assets = load_assets_from_modules([postgres])
bigquery_assets = load_assets_from_modules([bigquery])

defs = Definitions(
    assets=[licensor_metrics_dbt_assets, *common_assets, *postgres_assets, *bigquery_assets],
    resources={
        "dbt": DbtCliResource(project_dir=licensor_metrics_project),
        "bigquery": bigquery_resource
    },
)