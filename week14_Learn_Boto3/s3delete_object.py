"""
Delete a single s3 object. ex. file1.txt
"""
import boto3
s3_resource = boto3.client("s3")
s3_resource.delete_object(
    Bucket='mybucket04142023-v1',
    Key='file1.txt'    
    )