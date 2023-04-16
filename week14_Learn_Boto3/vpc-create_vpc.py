#title: create VPC
import boto3
ec2client = boto3.client('ec2')
ec2client.create_vpc(CidrBlock='10.0.0.0/16', )
