from extract.PageViewParser import PageViewParser
from extract.extract_types import Ingestion
from extract.ingestion_executor import IngestionExecutor
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="localhost",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    ingestion_list = [
        Ingestion(
            schema='sor',
            name="pageviews",
            fields='ip_address, datetime, url, campaign_id, ad_creative_id, device_id, referer',
            file_format="text",
            file_path="../datasets/data/pageview.txt",
            header="true",
            parser=PageViewParser()
        ),
        Ingestion(
            schema='sor',
            name="customer_leads",
            fields='device_id, lead_id, registered_at, credit_decision, credit_decision_at, signed_at, revenue',
            file_format="csv",
            file_path="../datasets/data/customer_leads_funnel.csv",
            header="false",
            parser=None
        ),
        Ingestion(
            schema='sor',
            name="facebook_ads_media_costs",
            fields='clicks, cost, date, campaign_id, campaign_name, impression',
            file_format="json",
            file_path="../datasets/data/facebook_ads_media_costs.jsonl",
            header="true",
            parser=None
        ),
        Ingestion(
            schema='sor',
            name="google_ads_media_costs",
            fields='ad_creative_id, ad_creative_name, clicks, cost, date, campaign_id, campaign_name, impressions',
            file_format="json",
            file_path="../datasets/data/google_ads_media_costs.jsonl",
            header="true",
            parser=None
        )
    ]

    IngestionExecutor(spark_service, postgres_service).execute(ingestion_list)
