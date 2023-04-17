# create from snapshot to a EBS volume
import boto3
ec2 = boto3.client('ec2')
response = ec2.create_volume(
    AvailabilityZone='us-east-1b',
    Encrypted=True, 
    Size=12,
    SnapshotId='snap-0829e82593a9afb36',
    VolumeType='gp2',
)
print(response) # 

'''
{'AvailabilityZone': 'us-east-1b', 'CreateTime': datetime.datetime(2023, 4, 17, 1, 51, 12, tzinfo=tzutc()), 
 'Encrypted': True, 'Size': 12, 'SnapshotId': 'snap-0829e82593a9afb36', 'State': 'creating', 
'VolumeId': 'vol-03e28779c5b980e65', 'Iops': 100, 'Tags': [], 'VolumeType': 'gp2', 'MultiAttachEnabled': False, 
'ResponseMetadata': 
    {'RequestId': '4bb38abd-3d0b-4557-a99e-5a7704ce9f26', 
     'HTTPStatusCode': 200, 
     'HTTPHeaders': 
        {'x-amzn-requestid': '4bb38abd-3d0b-4557-a99e-5a7704ce9f26', 'cache-control': 'no-cache, no-store', 
        'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 
         'content-length': '605', 'date': 'Mon, 17 Apr 2023 01:51:12 GMT', 'server': 'AmazonEC2'}, 
     'RetryAttempts': 0
    }
}
'''