class QueryBuilder:
    @staticmethod
    def build_insert(schema, table_name, fields):
        return f"INSERT INTO {schema}.{table_name} ({fields}) VALUES {{}}"
