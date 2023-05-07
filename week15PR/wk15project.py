'''
1) Create a Standard SQS Queue using Python.
2) Create a Lambda function in the console with a Python 3.7 or higher runtime (boiler plate form)
3) Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing. (python time function)
4) Create an API gateway HTTP API type trigger.
5) Test the trigger to verify the message was sent.
6) Push your code to GitHub and include the link in your write up.
'''

#1) Create a Standard SQS Queue using Python (Execute in local Linux server)
import boto3

sqs = boto3.client('sqs')
response = sqs.create_queue(
    QueueName='OrderTrackingSQS'
)
print('Queue created')