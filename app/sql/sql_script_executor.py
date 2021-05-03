from utils.logging import logging


class SQLScriptExecutor:

    def __init__(self, postgres_service, root_path='./sql'):
        self.postgres_service = postgres_service
        self.root_path=root_path

    def execute(self, path, command, artifact, schema, table_names):
        for table_name in table_names:
            file_path = f"{self.root_path}/{path}/{command}_{artifact}_{schema}_{table_name}.sql"
            logging.info(f"executing {file_path}")
            self.postgres_service.execute_sql_file(file_path)
