# create from EBS volume to snapshot
import boto3
ec2 = boto3.client('ec2')

snapshot = ec2.create_snapshot(
    Description='create a snapshot from a pre-existing EBS volume for cloud9 EC2 instance',
    VolumeId='vol-0c33b9f56a1fd06f7',

)
print(snapshot)
'''
{'Description': 'create a snapshot from a pre-existing EBS volume for cloud9 EC2 instance',
 'Encrypted': False, 'OwnerId': 'xxxxxxx', 'Progress': '', 'SnapshotId': 'snap-05361e2be38c77368', 
 'StartTime': datetime.datetime(2023, 4, 17, 2, 48, 45, 580000, tzinfo=tzutc()), 
 'State': 'pending', 'VolumeId': 'vol-0c33b9f56a1fd06f7', 'VolumeSize': 10, 'Tags': [], 
 'ResponseMetadata': {'RequestId': '783c20b4-0ee5-4588-8458-52cf78dd95c6', 
                      'HTTPStatusCode': 200, 
                      'HTTPHeaders': {'x-amzn-requestid': '783c20b4-0ee5-4588-8458-52cf78dd95c6', 
                                      'cache-control': 'no-cache, no-store', 
                                      'strict-transport-security': 'max-age=31536000; includeSubDomains', 
                                      'content-type': 'text/xml;charset=UTF-8', 
                                      'content-length': '628', 'date': 'Mon, 17 Apr 2023 02:48:45 GMT', 
                                      'server': 'AmazonEC2'
                                     }, 
                      'RetryAttempts': 0
                     }
}
'''
