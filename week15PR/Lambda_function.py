import json, boto3, time
import os
from datetime import datetime

def lambda_handler(event, context): # Lambda function core logic
    #[1] Track time for client's purchase order.
    time_now = datetime.now()
    timestamp = time_now.strftime("%m-%D-%Y %H:%M:%S")
    print (f'The time of purcahsing order: {timestamp}')

    #[2] Send a message containing the above time to your SQS queue.
    sqs=boto3.client('sqs')
    sqs_response = sqs.send_message(
        QueueUrl = os.gentenv('QUEUEURL'),
        MessgeBody= timestamp
    )
    #[3] Transform the sqs_response format to string format
    #parsed_json = json.loads(sqs_response) # the JSON object must be str, bytes or bytearray
    #arranged_sqs_response = json.dumps(parsed_json, indent=4)
    
    arranged_sqs_response= json.dumps(sqs_response, indent=4) # transform the json object (dict format) to string format
    print(f"The outcome of sending message is:\n{arranged_sqs_response}")

    return { # show this result as Response in Execution results
        'statusCode' : 200,
        'body': json.dumps((f'The timestamp for the order is: ' + timestamp))
    }