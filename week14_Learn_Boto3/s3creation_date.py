# Display the creation time of your S3 buckets
import boto3
s3_resource=boto3.client('s3')
print(s3_resource.list_buckets())
'''
Output ==> {'ResponseMetadata': {'RequestId': '19SM6FBEPN6PPVW4', 'HostId': 'fFhqcFUvPXIyMxfLuxLmRV/SmOpqhsTZsg5EQiPjKsGlqGX7ElnZcLyTMknnQQ7Oy/XdjR/6KHg=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'fFhqcFUvPXIyMxfLuxLmRV/SmOpqhsTZsg5EQiPjKsGlqGX7ElnZcLyTMknnQQ7Oy/XdjR/6KHg=', 'x-amz-request-id': '19SM6FBEPN6PPVW4', 'date': 'Sat, 15 Apr 2023 12:50:45 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v1', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 0, 17, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v2', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 13, 37, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'doh.kim17', 'ID': '309b7daf8c23db95b80dfd3fe475e0e810eb7716cb2c9e9bb726cf827dc6b5a0'}}
'''
print(len(s3_resource.list_buckets())) 
# list_buckets() will retrieve a list of S3 buckets. Using len() method, it will now show the number of S3 buckets
# Output ==> 3 

print((s3_resource.list_buckets()).keys()) 
# Output ==> dict_keys(['ResponseMetadata', 'Buckets', 'Owner']) # Three keys 

print(s3_resource.list_buckets()['Buckets']) 
# print the value corresponding to key of 'Buckets' from the dictionary. => a list shown below
'''
[{'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v1', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 0, 17, tzinfo=tzlocal())}, {'Name': 'mybucket04142023-v2', 'CreationDate': datetime.datetime(2023, 4, 15, 3, 13, 37, tzinfo=tzlocal())}]
'''

print(s3_resource.list_buckets()['Buckets'][0]) #This is for your first bucket!
# Print the element at index 0 of the above list. see the output below.
# Output ==> {'Name': 'luit-gold-do-testmb', 'CreationDate': datetime.datetime(2023, 2, 10, 0, 59, 22, tzinfo=tzlocal())}

first_bucket_create = s3_resource.list_buckets()['Buckets'][0]['CreationDate']
print(first_bucket_create)
# print the date and time
# Output ==> 2023-02-10 00:59:22+00:00

creation_date_first_bucket = s3_resource.list_buckets()['Buckets'][0]['CreationDate'] 
print(creation_date_first_bucket.strftime("Month:%m Day:%d Year:%y; Time: %H:%M:%S"))  
# Change the format of the time using strftime() function
# Output ==> Month:02 Day:10 Year:23; Time: 00:59:22

######################
# I would like to retrieve all buckets' creation time info using for loop.
buckets_info = s3_resource.list_buckets()['Buckets']
print(type(buckets_info)) # Output ==> <class 'list'>

for each_bucket_info in buckets_info:
    print(f"The bucket '{each_bucket_info['Name']}' was created on {(each_bucket_info['CreationDate'].strftime('Month:%m Day:%d Year:%y; Time: %H:%M:%S'))}") 

''' Output below:
The bucket 'luit-gold-do-testmb' was created on Month:02 Day:10 Year:23; Time: 00:59:22
The bucket 'mybucket04142023-v1' was created on Month:04 Day:15 Year:23; Time: 03:00:17
The bucket 'mybucket04142023-v2' was created on Month:04 Day:15 Year:23; Time: 03:13:37
'''

#print('Modified output below using strftime() function ')
for each_bucket_info in buckets_info:
    print(f"The bucket '{each_bucket_info['Name']}' was created on {(each_bucket_info['CreationDate'].strftime('%m/%d/%Y; Time: %H:%M:%S'))}") 
'''
The bucket 'luit-gold-do-testmb' was created on 02/10/2023; Time: 00:59:22
The bucket 'mybucket04142023-v1' was created on 04/15/2023; Time: 03:00:17
The bucket 'mybucket04142023-v2' was created on 04/15/2023; Time: 03:13:37
'''

