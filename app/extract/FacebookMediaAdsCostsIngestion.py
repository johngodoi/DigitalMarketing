from pyspark.sql import SparkSession
import psycopg2

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("facebook media ads costs ingestion") \
    .getOrCreate()

df = spark.read\
    .format("json")\
    .option("header", "true")\
    .load("../../datasets/data/facebook_ads_media_costs.jsonl")

df.cache()
df.show()
df.printSchema()

conn = psycopg2.connect(
    host="localhost",
    database="marketing",
    user="admin",
    password="admin")

cur = conn.cursor()

insert_query = "INSERT INTO " \
               "sor.facebook_ads_media_costs " \
               "(clicks, cost, date, campaign_id, campaign_name, impression) VALUES {}"
facebook_seq = [insert_query.format(tuple(x)) for x in df.collect()]

for insert in facebook_seq:
    cur.execute(insert)

conn.commit()
cur.close()
conn.close()


