from extract.ingestion_executor import IngestionExecutor
from extract.insert_queries import insert_queries
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="localhost",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    ingestion_executor = IngestionExecutor(spark_service, postgres_service)
    ingestion_executor.execute(insert_queries["customer_leads"], "csv", "../datasets/data/customer_leads_funnel.csv", "false")
    ingestion_executor.execute(insert_queries["facebook"], "json", "../datasets/data/facebook_ads_media_costs.jsonl")
    ingestion_executor.execute(insert_queries["google"], "json", "../datasets/data/google_ads_media_costs.jsonl")
