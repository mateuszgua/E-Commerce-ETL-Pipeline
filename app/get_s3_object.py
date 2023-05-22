import csv

from s3_manager import get_s3_client
from config import Config


def get_object_from_s3(file_path):
    try:
        s3 = get_s3_client()
        obj = s3.get_object(Bucket=Config.AWS_BUCKET,
                            Key=file_path)
    except:
        print(f"Error with get list from s3 bucket")
    else:
        return obj