import boto3


class S3Handler:
    def uploadFile(file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket"""

    s3 = boto3.client("S3")
