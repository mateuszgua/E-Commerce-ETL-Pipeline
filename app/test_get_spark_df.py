import pytest
import pandas as pd
from pyspark.sql import SparkSession
import pyarrow as pa
from pyspark.sql.types import StructType, StructField, LongType, StringType

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession.builder.getOrCreate()
    yield spark
    spark.stop()

def test_create_dataframe_from_pyarrow(spark_session):
    table = pa.Table.from_pandas(pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}))

    spark_df = spark_session.createDataFrame(table.to_pandas())

    expected_schema = StructType([
        StructField('col1', LongType(), nullable=True),
        StructField('col2', StringType(), nullable=True)
    ])

    assert spark_df.schema == expected_schema

    spark_df_values = [list(row.asDict().values()) for row in spark_df.collect()]

    expected_values = [[1, 'A'], [2, 'B'], [3, 'C']]

    assert spark_df_values == expected_values
