import io
import pyarrow.parquet as pq

def get_pandas_df(s3_object):
        object_content = s3_object['Body'].read()
        bytes_io = io.BytesIO(object_content)
        table = pq.read_table(bytes_io)
        df_pandas = table.to_pandas()
        return df_pandas