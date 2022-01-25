
import os
from os.path import abspath
from minio import Minio
from pyspark.sql import SparkSession
from pyspark.sql.functions import date_format, current_timestamp

# Folders and Subfolders
BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
JARS_DIR = os.path.join(BASE_DIR, "jars")


# Starting spark
spark = (
    SparkSession.builder.appName("pipeline") 
    .config("spark.sql.warehouse.dir", abspath('spark-warehouse')) 
    .config("fs.s3a.endpoint", "http://172.25.0.3:9000") 
    .config("fs.s3a.access.key", "kay")
    .config("fs.s3a.secret.key", "minio2014")
    .config("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") 
    .config("fs.s3a.path.style.access", "True")
    .config("spark.jars", os.path.join(JARS_DIR, "postgresql-42.3.1.jar"))
    .getOrCreate())



# Configuration postgres:
config_file = {
    "url": "jdbc:postgresql:data",
    "driver": "org.postgresql.Driver",
    "user": "kay",
    "password": "pg2014",
    "host": "172.25.0.2",
    "port": "5432",
}


# Configuration minio:
client = Minio(
        "172.25.0.3:9000",
        access_key="kay",
        secret_key="minio2014",
        secure=False
    )

       
# Database reading
class Pipeline():
    def __init__(self, tables:list) -> None:
        self.tables = tables
        
    def create_buckets(self) -> None:
        """[Create the buckets in the data lake]
        """
        if client.bucket_exists("raw") and client.bucket_exists("bronze"):
            print("bucket exists")
        else:
            client.make_bucket("raw")
            client.make_bucket("bronze")
        
        
    def extract_data(self) -> None:
        """[Extract the data from the database and insert it into the raw layer]
        """
        for table in self.tables:
            df_ = spark.read.format("jdbc").option("dbtable",table).options(**config_file).load()
            df_ = df_.withColumn("extracted_at", date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss'))
            df_.write.format("parquet").mode("overwrite").partitionBy("extracted_at").save(f"s3a://raw/{table}.parquet")


    def transform_data(self) -> None:
        """[Transform the data and insert it into the bronze layer]
        """
        for table in self.tables:
            df = spark.read.format("parquet").load(f"s3a://raw/{table}.parquet")
            columns_name = ["data_cadastro","data_atribuicao_medalha","data_expiracao_medalha","data_removida_medalha","data_updated","data_aniversario"]
            for item in df.columns:
                if item in columns_name:
                    df = df.withColumn(item, df[item].cast("timestamp"))
                else:
                    pass
            df = df.withColumn("created_at", date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss'))
            df.write.format("parquet").mode("overwrite").partitionBy("created_at").save(f"s3a://bronze/{table}.parquet")


if __name__ == "__main__":
    db = Pipeline(["tb_players","tb_players_medalha","tb_lobby_stats_player"])
    db.create_buckets()
    db.extract_data()
    db.transform_data()


