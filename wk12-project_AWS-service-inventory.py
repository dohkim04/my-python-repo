#!/usr/bin/env python3.7

# Week 12 mini project
# Title: AWS Service Inventory

# Create a list of services using Python. ex. S3, Lambda, EC2, etc.

# Instruction:
print("1. The list should be empty initially.")
aws_service_list = []
print("The initial status of aws_service_list:", aws_service_list)

# Output:
# ~/environment/my-python-repo (week12-mini-project) $ python3.7 wk12-project_AWS-service-inventory.py 
# []


print("2. Populate the list using append or insert.")
aws_service_list.append('EC2')
aws_service_list.append('Lambda')
aws_service_list.append('Lightsail')
aws_service_list.append('ECR')
aws_service_list.append('ECS')
print("The initial service list using append:", aws_service_list)

aws_service_list.insert(3,'S3')
print("After inserting 'S3' at index 3:", aws_service_list)

aws_service_list.insert(5,'EFS')
print("After inserting 'EFS' at index 6:", aws_service_list)

aws_service_list.insert(-1,'Glacier')
print("After inserting 'Goacier' before index -1:", aws_service_list)

aws_service_list.insert(0, 'VPC')
print("After inserting 'VPC' at index 0:", aws_service_list)

aws_service_list.insert(-4,'AppSync')
print("After inserting 'AppSync' before index -4:", aws_service_list)

# added comments
print("Note:")
print("When using a minus index number, a new element will be added before the designated index number")
print('When using a positive index number, a new element will be added at the designated index number')

# Printed output
'''
~/environment/my-python-repo (week12-mini-project) $ python3.7 wk12-project_AWS-service-inventory.py 
[]
The initial service list: ['EC2', 'Lambda', 'Lightsail', 'ECR', 'ECS']
After adding 'S3' at index 3: ['EC2', 'Lambda', 'Lightsail', 'S3', 'ECR', 'ECS']
After adding 'EFS' at index 6: ['EC2', 'Lambda', 'Lightsail', 'S3', 'ECR', 'EFS', 'ECS']
After adding 'Goacier' before index -1: ['EC2', 'Lambda', 'Lightsail', 'S3', 'ECR', 'EFS', 'Glacier', 'ECS']
After adding 'VPC' at index 0: ['VPC', 'EC2', 'Lambda', 'Lightsail', 'S3', 'ECR', 'EFS', 'Glacier', 'ECS']
After adding 'AppSync' before index -4: ['VPC', 'EC2', 'Lambda', 'Lightsail', 'S3', 'AppSync', 'ECR', 'EFS', 'Glacier', 'ECS']
Note:
When using a minus index number, a new element will be added before the designated index number
When using a positive index number, a new element will be added at the designated index number
'''

# 3. Print the list and the length of the list.
print('\n=================================\nAWS Service List: ', aws_service_list)
print("The length of the aws_service_list: ", len(aws_service_list))

"""
4. Remove two specific services from the list by name or by index.
5. Print the new list and the new length of the list.
6. Push your code to GitHub and include the link in your LinkedIn write-up.
"""

'''
Below is a selected list of common AWS services below.
Compute (EC2, Lightsail, Lambda, EB, Outposts)
Containers (ECR, ECS, EKS)
Storage (S3, EFS, FSx, S3 Glacier, Storage Gateway)
Database (RDS, ElastiCache, DynamoDB, MemoryDB for Redis)
Migration & Transfer (Snow Family, DataSync)
Networking & Content Delivery (VPC, CloudFront, Route 53, API Gateway)
Developer Tools(CodeCommit, CodeBuild, CodeDeploy, CodePipeline, Cloud9, X-Ray, AppConfig)
Management & Governance (Organizations, CloudWatch, Auto Scaling, CloudFormation, Config, Systems Manager, License Manager, Health Dashboard, CloudTrail)
Analytics (Athena, Redshift, EMR, OpenSearch, Kinesis, QuickSight, DataPipeline, Glue)
Security, Identity & Compliance (IAM, Cognito, Secrets Manager, GuardDuty, Inspector, Macie, KMS, CloudHSM, WAF, Shield, Private Certificate Authority)
AWS Cost Management (Cost Explorer, Budgets, Marketplace)
Front-end Web & Mobile (Amplify, AppSync)
Application Integration (Step Functions, EventBridge, SNS, SQS, SWF)
Business Applications (Connect, Chime, SES, Alexa)
'''



