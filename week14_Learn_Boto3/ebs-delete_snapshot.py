# delete snapshots
import boto3
ec2client=boto3.client('ec2')
response=ec2client.delete_snapshot(
    SnapshotId='snap-05361e2be38c77368',
)

print(response)

'''
{'ResponseMetadata': {'RequestId': '6d01fda4-160d-45c6-aa69-0ebc9e721b76', 'HTTPStatusCode': 200, 
                      'HTTPHeaders': {'x-amzn-requestid': '6d01fda4-160d-45c6-aa69-0ebc9e721b76', 
                                      'cache-control': 'no-cache, no-store', 
                                      'strict-transport-security': 'max-age=31536000; includeSubDomains', 
                                      'content-type': 'text/xml;charset=UTF-8', 
                                      'content-length': '229', 
                                      'date': 'Mon, 17 Apr 2023 03:33:48 GMT', 'server': 'AmazonEC2'
                                      }, 
                      'RetryAttempts': 0
                     }
}
'''