from invoke import task
import psycopg2
from app.utils.logging import logging


@task
def check_and_wait_db_availability(c):
    while not is_available():
        logging.info("waiting for db be available")
    logging.info("db ready")


@task(check_and_wait_db_availability)
def execute_migration(c):
    logging.info("executing alembic db migration")
    c.run("alembic upgrade head")


def is_available():
    try:
        conn = psycopg2.connect("dbname='marketing' user='admin' host='localhost' password='admin' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False
