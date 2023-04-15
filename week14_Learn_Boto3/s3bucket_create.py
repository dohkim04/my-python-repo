"""
Your module description
"""
import boto3
#s3=boto3.resource('s3')
s3=boto3.client('s3')
#bucket=s3.bucket("mybucket4142023-v1") # This is another way of putting a new bucket name usinb bucket() function
create_response = s3.create_bucket(
    ACL='private',                  # Previously, 'public-read' is chosen for 'mybucket04142023-v1' bucket 
    Bucket = 'mybucket04142023-v2', # Previously, Bucket name as 'mybucket04142023-v1' 
    CreateBucketConfiguration={'LocationConstraint': 'us-east-2'},) # Note: us-east-1 was not listed so us-east-2 was chosen instead.
print(create_response)
#print(len(response))
print("\nNext, let\'s list up current bucket list below")

list_response = s3.list_buckets()
buckets = list_response['Buckets']
for bucket in buckets:
    print(bucket['Name'])

''' Output is shown below:
{'ResponseMetadata': {'RequestId': '5DRBYGHAZYTXV2PZ', 'HostId': '4+qInLjxhVGWDyUPMK2a+Ck/DpvuZxs6/9qI8RkJejQqcCraWMFZEImwy2q96CjsgNCIg8Wh1mg=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': '4+qInLjxhVGWDyUPMK2a+Ck/DpvuZxs6/9qI8RkJejQqcCraWMFZEImwy2q96CjsgNCIg8Wh1mg=', 'x-amz-request-id': '5DRBYGHAZYTXV2PZ', 'date': 'Sat, 15 Apr 2023 03:00:17 GMT', 'location': 'http://mybucket04142023-v1.s3.amazonaws.com/', 'server': 'AmazonS3', 'content-length': '0'}, 'RetryAttempts': 0}, 'Location': 'http://mybucket04142023-v1.s3.amazonaws.com/'}


Traceback (most recent call last):
  File "/home/ec2-user/environment/my-python-repo/week14/s3bucket_create.py", line 15, in <module>
    print(response['Buckets'])
KeyError: 'Buckets'

[Case 2: After fixing codes for list_buckets and create_bucket]

{'ResponseMetadata': {'RequestId': '8RR6C0YSFRX1636C', 'HostId': 'sUcebljRowOLajzpiLbdASY5Wi4kNYqaqwwmIZF4BeFx+1zstesj7PfYOEkpibnmI9akGHm1esM=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'sUcebljRowOLajzpiLbdASY5Wi4kNYqaqwwmIZF4BeFx+1zstesj7PfYOEkpibnmI9akGHm1esM=', 'x-amz-request-id': '8RR6C0YSFRX1636C', 'date': 'Sat, 15 Apr 2023 03:13:37 GMT', 'location': 'http://mybucket04142023-v2.s3.amazonaws.com/', 'server': 'AmazonS3', 'content-length': '0'}, 'RetryAttempts': 0}, 'Location': 'http://mybucket04142023-v2.s3.amazonaws.com/'}

Next, let's list up current bucket list below
luit-gold-do-testmb
mybucket04142023-v1
mybucket04142023-v2

'''