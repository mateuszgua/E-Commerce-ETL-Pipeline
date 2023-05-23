import io

from pyspark.sql import SparkSession

from config import Config


config = Config()


def get_df_spark(pandas_df):
    try:
        spark = SparkSession.builder.appName('Read Parquet from Bytes').getOrCreate()
        spark_df = spark.createDataFrame(pandas_df)
        spark.stop()
    except Exception as e:
        print(f"Error with create dataframe: {e}")
    else:
        return spark_df
    
