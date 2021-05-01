from extract.facebook_media_ads_costs_ingestion import FacebookMediaAdsCostsIngestion
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="localhost",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    facebook_media_ads_costs_ingestion = FacebookMediaAdsCostsIngestion(spark_service, postgres_service)
    facebook_media_ads_costs_ingestion.execute()
