from invoke import task
import psycopg2

@task
def check_and_wait_db_availability(c):
    while not is_available():
        print("waiting for db be available")
    print("db ready")


def is_available():
    try:
        conn = psycopg2.connect("dbname='marketing' user='admin' host='localhost' password='admin' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False