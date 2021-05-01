class IngestionExecutor:

    def __init__(self, spark_service, postgres_service):
        self.spark_service = spark_service
        self.postgres_service = postgres_service

    def execute(self, insert_query, file_format, file_path, header="true", parser=None):
        df = self.spark_service.load_file(file_format, file_path, header)
        if parser:
            values_in_memory = parser.parse(df)
        else:
            values_in_memory = [tuple(x) for x in df.collect()]
        self.postgres_service.insert(insert_query, values_in_memory)


