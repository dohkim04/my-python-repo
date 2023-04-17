#title: delete/remove VPC
import boto3
ec2client = boto3.client('ec2')
x= ec2client.delete_vpc(
    VpcId='vpc-0b67bb169e26cfd3a',
)
print(x)
'''
{'ResponseMetadata': 
    {'RequestId': '24e4da14-c7bd-4fd2-af8f-0212dfe0e1bf', 
    'HTTPStatusCode': 200, 
    'HTTPHeaders': {'x-amzn-requestid': '24e4da14-c7bd-4fd2-af8f-0212dfe0e1bf', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '219', 'date': 'Sun, 16 Apr 2023 20:08:46 GMT', 'server': 'AmazonEC2'}, 
    'RetryAttempts': 0
    }
}
With the API result on screenshot, the vpc with VpcId "vpc-0b67bb169e26cfd3a" was removed and it was confirmed from AWS console. 
'''
