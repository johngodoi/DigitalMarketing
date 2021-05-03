from utils.logging import logging


class SQLScriptExecutor:

    def __init__(self, postgres_service):
        self.postgres_service = postgres_service

    def execute(self, sql_scripts):
        for file in sql_scripts:
            logging.info(f"executing {file}")
            self.postgres_service.execute_sql_file(file)
