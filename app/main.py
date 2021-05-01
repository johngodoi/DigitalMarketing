from extract.customer_leads_ingestion import CustomerLeadsIngestion
from extract.facebook_media_ads_costs_ingestion import FacebookMediaAdsCostsIngestion
from extract.google_media_ads_costs_ingestion import GoogleMediaAdsCostsIngestion
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="localhost",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    customer_leads_ingestion = CustomerLeadsIngestion(spark_service, postgres_service)
    customer_leads_ingestion.execute()
    google_media_ads_costs_ingestion = GoogleMediaAdsCostsIngestion(spark_service, postgres_service)
    google_media_ads_costs_ingestion.execute()
    facebook_media_ads_costs_ingestion = FacebookMediaAdsCostsIngestion(spark_service, postgres_service)
    facebook_media_ads_costs_ingestion.execute()
