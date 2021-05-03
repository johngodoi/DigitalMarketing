import yaml

from extract.ingestion_executor import IngestionExecutor
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService
from sql.sql_script_executor import SQLScriptExecutor
from utils.logging import logging

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="postgres",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    with open("../datasets/configuration/ingestions.yml", 'r') as stream:
        ingestion_list = yaml.safe_load(stream)

    IngestionExecutor(spark_service, postgres_service).execute(ingestion_list)

    with open("../datasets/configuration/sql_scripts.yml", 'r') as stream:
        sql_scripts = yaml.safe_load(stream)

    SQLScriptExecutor(postgres_service).execute(sql_scripts)

    logging.info("That is it!")

