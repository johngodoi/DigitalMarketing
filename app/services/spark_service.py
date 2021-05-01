from pyspark.sql import SparkSession


class SparkService:

    def __init__(self, app_name, master="local[*]"):
        self.app_name = app_name
        self.master = master
        self.spark = SparkSession.builder \
            .master(master) \
            .appName(app_name) \
            .getOrCreate()

    def load_file(self, file_format, file_path):
        return self.spark.read \
            .format(file_format) \
            .option("header", "true") \
            .load(file_path)
