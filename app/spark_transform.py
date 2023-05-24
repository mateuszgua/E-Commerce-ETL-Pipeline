from get_s3_object import get_object_from_s3
from get_spark_df import get_df_spark
from get_pandas_df import get_pandas_df

from config import Config

def transform_test():
    s3_object = get_object_from_s3(Config.FILE_PATH_TEST) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df
        
def transform_train():
    s3_object = get_object_from_s3(Config.FILE_PATH_TRAIN) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df

def transform_val():
    s3_object = get_object_from_s3(Config.FILE_PATH_VAL) 
    pandas_df = get_pandas_df(s3_object)
    df = get_df_spark(pandas_df)
    return df