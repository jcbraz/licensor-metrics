from setuptools import find_packages, setup

setup(
    name="metrics_pipeline",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "metrics_pipeline": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-gcp",
        "dagster-gcp-pandas"
        "dagster-dbt",
        "polars",
        "pyarrow",
        "connectorx",
        "loguru",
        "dbt-snowflake<1.9",
        "dbt-snowflake<1.9",
        "dbt-clickhouse<1.9",
        "dbt-postgres<1.9",
        "dbt-postgres<1.9",
        "dbt-snowflake<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)