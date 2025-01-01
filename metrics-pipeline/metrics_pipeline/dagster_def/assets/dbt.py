from pathlib import Path
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets, DbtProject


licensor_metrics_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "..", "dbt").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "..", "dbt-project").resolve(),
)
licensor_metrics_project.prepare_if_dev()

@dbt_assets(manifest=licensor_metrics_project.manifest_path)
def licensor_metrics_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()