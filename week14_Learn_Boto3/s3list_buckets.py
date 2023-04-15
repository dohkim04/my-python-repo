"""
Your module description
"""
import boto3
#s3=boto3.resource('s3')
s3=boto3.client('s3')
response=s3.list_buckets()
#bucket=s3.bucket("mybucket4142023-v1")
#response = client.create_bucket(
#    ACL='public-read',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'us-east-1'},)
print(response)
#print(len(response))
print("\n")
print(response['Buckets'])

''' Output is shown below:
[Case 1: Initial status]
{'ResponseMetadata': {'RequestId': 'SJ4BMGE7VT5NNJAN', 'HostId': '//+jz4Gdek2s8WDmn7ScesmnxpCCx/VbhbANUFMg7Jrgyz/CqQp6e0elXZCMuDgz1efpj9lDP0Q=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': '//+jz4Gdek2s8WDmn7ScesmnxpCCx/VbhbANUFMg7Jrgyz/CqQp6e0elXZCMuDgz1efpj9lDP0Q=', 'x-amz-request-id': 'SJ4BMGE7VT5NNJAN', 'date': 'Sat, 15 Apr 2023 02:45:39 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'doh.kim17', 'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}


[{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}]


[Case 2] - after creating one more bucket in us-east-2
{'ResponseMetadata': {'RequestId': '0DXP3S5G9T5ED3NR', 'HostId': 'R3gZrpREz6vdQmfP4n5+gqkfjPwSDvM/vo4TVQESZh43FhXKHA9+CpXKLBuq8daa3O9sAqhewDI=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'R3gZrpREz6vdQmfP4n5+gqkfjPwSDvM/vo4TVQESZh43FhXKHA9+CpXKLBuq8daa3O9sAqhewDI=', 'x-amz-request-id': '0DXP3S5G9T5ED3NR', 'date': 'Sat, 15 Apr 2023 03:00:55 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v1', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 0, 17, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'doh.kim17', 'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}


[{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v1', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 0, 17, tzinfo=tzlocal())}]
'''