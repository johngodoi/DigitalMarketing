from extract.query_builder import QueryBuilder
from extract.PageViewParser import PageViewParser
from utils.logging import logging


class IngestionExecutor:

    def __init__(self, spark_service, postgres_service):
        self.spark_service = spark_service
        self.postgres_service = postgres_service

    def execute(self, ingestion_list):
        for ingestion in ingestion_list:
            logging.info(f"executing {ingestion}")
            self._execute(
                insert_query=QueryBuilder.build_insert(ingestion['schema'], ingestion['name'], ingestion['fields']),
                file_format=ingestion['file_format'],
                file_path=ingestion['file_path'],
                header=ingestion['header'],
                parser=eval(ingestion['parser']) if ingestion['parser'] else None
            )
        logging.info("ingestions executed")

    def _execute(self, insert_query, file_format, file_path, header="true", parser=None):
        df = self.spark_service.load_file(file_format, file_path, header)
        if parser:
            values_in_memory = parser.parse(df)
        else:
            values_in_memory = [tuple(x) for x in df.collect()]
        logging.info(f"inserting {len(values_in_memory)} with {insert_query}" )
        self.postgres_service.insert(insert_query, values_in_memory)


