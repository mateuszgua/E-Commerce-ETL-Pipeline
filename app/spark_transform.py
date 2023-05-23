from get_s3_object import get_object_from_s3
from get_spark_df import get_df_spark
from get_pandas_df import get_pandas_df

file_path_test = 'data/source/test.parquet'
file_path_train = 'data/source/train.parquet'
file_path_val = 'data/source/val.parquet'

def transform_test():
    s3_object = get_object_from_s3(file_path_test) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df
        
def transform_train():
    s3_object = get_object_from_s3(file_path_train) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df

def transform_val():
    s3_object = get_object_from_s3(file_path_val) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df