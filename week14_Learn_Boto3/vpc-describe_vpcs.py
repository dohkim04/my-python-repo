#title: Describe VPCs
import boto3
ec2client = boto3.client('ec2')
x = ec2client.describe_vpcs()
print (x['Vpcs'])
no_of_vpcs = x['Vpcs']
#print(len(no_of_vpcs)) # 3
for vpc in no_of_vpcs:
    print(f"CIDR Block: {vpc['CidrBlock']}; VpcId: {vpc['VpcId']}; Is it default VPC? {vpc['IsDefault']}")
'''
172.31.0.0/16
10.0.0.0/16
89.0.0.0/16
'''
