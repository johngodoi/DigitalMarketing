class CustomerLeadsIngestion:

    insert_query = "INSERT INTO " \
                   "sor.customer_leads " \
                   "(device_id, lead_id, registered_at, credit_decision, credit_decision_at, signed_at, revenue) " \
                   "VALUES {}"

    def __init__(self, spark_service, postgres_service):
        self.spark_service = spark_service
        self.postgres_service = postgres_service

    def execute(self):
        df = self.spark_service.load_file("csv", "../datasets/data/customer_leads_funnel.csv", "false")
        values_in_memory = [tuple(x) for x in df.collect()]
        self.postgres_service.insert(CustomerLeadsIngestion.insert_query, values_in_memory)







