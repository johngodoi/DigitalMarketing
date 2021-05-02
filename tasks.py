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


@task
def truncate_sor(c):
    conn = psycopg2.connect("dbname='marketing' user='admin' host='postgres' password='admin' connect_timeout=1 ")
    tables = [
        "facebook_ads_media_costs",
        "google_ads_media_costs",
        "pageviews",
        "customer_leads"
    ]
    cursor = conn.cursor()
    for table in tables:
        logging.info(f"truncating sor.{table}")
        cursor.execute(f"truncate sor.{table} cascade")
    conn.commit()
    cursor.close()
    conn.close()


def is_available():
    try:
        conn = psycopg2.connect("dbname='marketing' user='admin' host='postgres' password='admin' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False
