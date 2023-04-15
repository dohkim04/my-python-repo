import boto3
# list s3 objects from a bucket
s3_resource = boto3.client("s3")
objects = s3_resource.list_objects(Bucket="mybucket04142023-v1", )["Contents"] # dict to list
#print(type(objects)) # <class 'list'>
#print(objects)
''' The commented 2 print statements will give the following results:
<class 'list'>
[{'Key': 'file1.txt', 'LastModified': datetime.datetime(2023, 4, 15, 3, 32, 30, tzinfo=tzlocal()), 'ETag': '"826e8142e6baabe8af779f5f490cf5f5"', 'Size': 5, 'StorageClass': 'STANDARD', 'Owner': {'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}, {'Key': 'file2.txt', 'LastModified': datetime.datetime(2023, 4, 15, 3, 32, 30, tzinfo=tzlocal()), 'ETag': '"1c1c96fd2cf8330db0bfa936ce82f3b9"', 'Size': 5, 'StorageClass': 'STANDARD', 'Owner': {'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}, {'Key': 'file4_uploaded.txt', 'LastModified': datetime.datetime(2023, 4, 15, 16, 45, 11, tzinfo=tzlocal()), 'ETag': '"6b2a0ab02ad1b251d3c0fe1572c63920"', 'Size': 28, 'StorageClass': 'STANDARD', 'Owner': {'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}, {'Key': 'file5_uploaded.txt', 'LastModified': datetime.datetime(2023, 4, 15, 16, 45, 11, tzinfo=tzlocal()), 'ETag': '"cbf98d04ccd96b7b8a34b16ced467bea"', 'Size': 28, 'StorageClass': 'STANDARD', 'Owner': {'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}, {'Key': 'file6_uploaded.txt', 'LastModified': datetime.datetime(2023, 4, 15, 16, 45, 12, tzinfo=tzlocal()), 'ETag': '"917ab25005d5c0122dd47097e4f2f87c"', 'Size': 28, 'StorageClass': 'STANDARD', 'Owner': {'ID': '309b7daf8c23db95file1.txt
'''
for object in objects:
    print(object['Key']) # another dictionary again. the value corresponding to "Key" 
'''Output printing all the objects in the s3 bucket.
file2.txt
file4_uploaded.txt
file5_uploaded.txt
file6_uploaded.txt
'''