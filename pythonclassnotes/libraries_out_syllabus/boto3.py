import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.resource("s3", config=Config(signature_version=UNSIGNED))
bucket = s3.Bucket("file1")

for obj in bucket.objects.filter(Prefix="json"):
    print(obj)