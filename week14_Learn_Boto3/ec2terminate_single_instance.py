#  ec2 terminate instances
import boto3
ec2 = boto3.client("ec2")
x = ec2.terminate_instances(
    InstanceIds=[
        'i-00c11fd80d3949d60','i-0f295b59ca67a119c','i-0d0d4dd212433ce81'
    ],

)



