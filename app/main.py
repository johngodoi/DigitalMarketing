import yaml

from extract.ingestion_executor import IngestionExecutor
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="postgres",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    with open("../datasets/configuration/ingestions.yml", 'r') as stream:
        ingestion_list = yaml.safe_load(stream)

    IngestionExecutor(spark_service, postgres_service).execute(ingestion_list)

