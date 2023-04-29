# This python code set up a session for an IAM role with temporary credentials
# You no longer need to hard-code (write) your AWS Access Key and Secret Key in this python code.
# procedure:
# 1. install and configure awscli on your local Linux server: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
# 2. In your local Linux server, execute "aws --version" command to check the status of your installed awscli
# 3. In your AWS console, select your IAM user and create the Access Key and Secret Key.
# 4. In your local Linux server, execute "aws configure" command and enter access key, secret key, region name, then set "json" for your data type
# 5. 
# 7. In your AWS console, create role and select IAM, roles, Create roles and follow the instruction. Obtain the ARN for the role.
# create or update the "config" file in ~/.aws/ directory of your local Linux system with the following 3 lines below:
# [profile xxxxxxxxx]
#    role_arn = arn:aws:iam::/<AWS-Account_Number>:role/<your-role-name>
#    source_profile = default
#
# Whenever you execute awscli, make sure to add '--profile xxxxxxxxx' on your awscli command.

import boto3
session = boto3.Session(profile_name="xxxxxxxxx")
s3 = session.client('s3')
print(s3.list_buckets())

print("=================")
dynamodb = session.resource('dynamodb', region_name="yyyyyy")
print(f"{dynamodb} is now being created as a DynamoDB resource object.\n") # check if your AWS SDK works properly. 
    # Output: dynamodb.ServiceResource() is now being created as a DynamoDB resource object.

print("=================")

client = session.client('iam')
response = client.list_roles(
    #PathPrefix='string',
    #Marker='string',
    #MaxItems=123
)
print(response)