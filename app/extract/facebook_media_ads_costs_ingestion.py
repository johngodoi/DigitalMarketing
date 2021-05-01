class FacebookMediaAdsCostsIngestion:

    insert_query = "INSERT INTO " \
                   "sor.facebook_ads_media_costs " \
                   "(clicks, cost, date, campaign_id, campaign_name, impression) VALUES {}"

    def __init__(self, spark_service, postgres_service):
        self.spark_service = spark_service
        self.postgres_service = postgres_service

    def execute(self):
        df = self.spark_service.load_file("json", "../datasets/data/facebook_ads_media_costs.jsonl")
        values_in_memory = [tuple(x) for x in df.collect()]
        self.postgres_service.insert(FacebookMediaAdsCostsIngestion.insert_query, values_in_memory)







