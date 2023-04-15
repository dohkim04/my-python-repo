import boto3
# upload a single file file4_uploaded.txt to the s3 bucket
# the bucket should be alredy created before executing this script. 
s3_resource = boto3.client("s3")
s3_resource.upload_file(
    Filename="s3files/file4_upload_by_Python.txt",
#    Filename="s3files/file1.txt",
    Bucket="mybucket04142023-v1", 
    Key="file4_uploaded.txt")
#    Key="file1.txt")
