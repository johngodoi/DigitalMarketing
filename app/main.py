import yaml

from extract.ingestion_executor import IngestionExecutor
from services.postgres_service import PostgreSQLService
from services.spark_service import SparkService
from sql.sql_script_executor import SQLScriptExecutor

if __name__ == '__main__':
    spark_service = SparkService(app_name="ingestion")
    postgres_service = PostgreSQLService(host="postgres",
                                         database="marketing",
                                         user="admin",
                                         password="admin")
    with open("../datasets/configuration/ingestions.yml", 'r') as stream:
        ingestion_list = yaml.safe_load(stream)

    IngestionExecutor(spark_service, postgres_service).execute(ingestion_list)

    sql_script_executor = SQLScriptExecutor(postgres_service)
    sql_script_executor.execute("transformation", "create", "table", "sot", [
        "dim_campaign_media",
        "dim_customer_lead",
        "dim_viewer",
        "fact_campaign_cost_effectiveness",
        "fact_credit_decision",
        "fact_customer_signature",
        "fact_page_views"
    ])
    sql_script_executor.execute("specialized", "create", "table", "espec", [
        "campaign_clicks",
        "campaign_costs",
        "campaign_leads",
        "campaign_revenue",
    ])
    sql_script_executor.execute("specialized", "create", "view", "espec", [
        "campaign_efficiency"
    ])

