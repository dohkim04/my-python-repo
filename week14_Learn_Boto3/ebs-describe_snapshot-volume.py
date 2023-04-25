# create EBS volume snapshots
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_snapshots(

    SnapshotIds=['snap-05361e2be38c77368','snap-0829e82593a9afb36'],
)

print(response) # 

'''

{'Snapshots': [{'Description': 'create a snapshot from a pre-existing EBS volume for cloud9 EC2 instance', 
                'Encrypted': False, 'OwnerId': 'xxxxxx', 'Progress': '100%', 'SnapshotId': 'snap-05361e2be38c77368', 
                'StartTime': datetime.datetime(2023, 4, 17, 2, 48, 45, 580000, tzinfo=tzutc()), 'State': 'completed', 
                'VolumeId': 'vol-0c33b9f56a1fd06f7', 'VolumeSize': 10, 'StorageTier': 'standard'
               }, 
               {'Description': 'create a snapshot to create a volume using Boto3', 'Encrypted': False, 
                'OwnerId': 'xxxxx', 'Progress': '100%', 'SnapshotId': 'snap-0829e82593a9afb36', 
                'StartTime': datetime.datetime(2023, 4, 17, 1, 30, 58, 428000, tzinfo=tzutc()), 
                'State': 'completed', 'VolumeId': 'vol-0c33b9f56a1fd06f7', 'VolumeSize': 10, 
                'Tags': [{'Key': 'Name', 'Value': 'EBS snapshot'}], 
                'StorageTier': 'standard'
               }], 
 'ResponseMetadata': {'RequestId': '7b49237f-8a77-4d87-9a63-8387644d734d', 'HTTPStatusCode': 200, 
                      'HTTPHeaders': {'x-amzn-requestid': '7b49237f-8a77-4d87-9a63-8387644d734d', 
                                      'cache-control': 'no-cache, no-store', 
                                      'strict-transport-security': 'max-age=31536000; includeSubDomains', 
                                      'content-type': 'text/xml;charset=UTF-8', 'content-length': '1531', 
                                      'date': 'Mon, 17 Apr 2023 03:13:37 GMT', 
                                      'server': 'AmazonEC2'
                                     }, 
 'RetryAttempts': 0}
 }
'''
