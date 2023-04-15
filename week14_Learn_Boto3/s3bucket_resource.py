"""
Your module description
"""
import boto3
s3_resource=boto3.resource('s3')
# print(s3_resource) # Output ==> s3.ServiceResource()
for bucket in s3_resource.buckets.all():
    #print(bucket) # Output ==> s3.Bucket(name='luit-gold-do-testmb')  s3.Bucket(name='mybucket04142023-v1') s3.Bucket(name='mybucket04142023-v2')
    print(bucket.name) 

bucket_list = list(s3_resource.buckets.all())
print(f"This is a list of buckets: {bucket_list}")
print(f"The size of a list of buckets: {len(bucket_list)}")
'''Output:

luit-gold-do-testmb
mybucket04142023-v1
mybucket04142023-v2
This is a list of buckets: [s3.Bucket(name='luit-gold-do-testmb'), s3.Bucket(name='mybucket04142023-v1'), s3.Bucket(name='mybucket04142023-v2')]
The size of a list of buckets: 3
'''

## Below is a reference from https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
#s3 = boto3.resource('s3')
#bucket = s3.Bucket('my-bucket')
#for obj in bucket.objects.all():
#    print(obj.key)
