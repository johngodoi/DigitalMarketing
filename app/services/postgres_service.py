import psycopg2


class PostgreSQLService:

    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)

    def execute_sql_file(self, file):
        cur = self.conn.cursor()
        cur.execute(open(file, "r").read())
        self.conn.commit()
        cur.close()

    def insert(self, statement, values):
        cur = self.conn.cursor()
        records_list_template = ','.join(['%s'] * len(values))
        cur.execute(statement.format(records_list_template), values)
        self.conn.commit()
        cur.close()

    def close(self):
        self.conn.close()
