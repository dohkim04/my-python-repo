# This code is used for the lambda function in AWS Lambda.
# Design: 
# ##  Once cloudWatch Event senses EC2 instante state change as running state,
# ##  it will trigger this Lambda code to check 
# ##  whether the running EC2 instance has Key value of either "SPECIAL_EDITION" or "aws:cloud9:owner".
# ##  If the EC2 instance does not meet the above requirement, then the Lambda stop the instance and email to the user via SNS.  
import json, boto3
ec2client = boto3.client('ec2')  # create ec2client service object connecting to AWS EC2 service
snsclient = boto3.client('sns')  # create snsclient service object connecting to AWS SNS service
def lambda_handler(event, context): 
    # TODO implement
    ec2_instance_id = event['detail']['instance-id'] # retrieve EC2 Instance ID from an event, an input data for this lamba function 
    tag_response = ec2client.describe_tags(  # Filter the ec2 client service object based on the EC2 Instance ID and create tag_response data.
        Filters=[{'Name': 'resource-id', 'Values': [ec2_instance_id,],},],
    )
    print(tag_response)
    
    # let's flag as 'STOP' for EC2 Instances without the Key value of appropriate tags, either "SPECIAL_EDITION " or "aws:cloud9:owner"
    flag ='STOP'  # Assume that the default for flag variable is set to 'STOP' per given tag_response. 
    alltags = tag_response['Tags'] # retrieve alltags dictionary that is the value of the 'Tags' key the in tag_response dictionary.
    for each_tag in alltags:       # loop through each component within the alltags dictionary.
        print(each_tag['Key'])
        if (each_tag['Key'] == 'SPECIAL_EDITION' or each_tag['Key'] == 'aws:cloud9:owner'):
            flag = "DONT_STOP"    
            break
            
    print(flag) # give flag output per Key value per EC2 instance    
    
    # stop EC2 instance and send email message via SNS topic
    if flag == "STOP":
        ec2response = ec2client.stop_instances(InstanceIds=[ec2_instance_id,],)
        print(ec2response)
        snsresponse = snsclient.publish(
        TopicArn='arn:aws:sns:us-east-1:xxxxxxxxxx:Warning_about_your_EC2',
        Message='Warning! Your EC2 stopped. You are not authorized to run the instances. Contact IT department.',
        Subject='doh.kim04@gmail.com',
)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

####
