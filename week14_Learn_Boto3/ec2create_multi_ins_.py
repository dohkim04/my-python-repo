#  launch EC2
import boto3
ec2 = boto3.resource("ec2")
ec2.create_instances( 
    ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MaxCount=4,
    MinCount=2,
)
'''Output: no message was displayed upon execution
$ python3 ec2create_instances.py 
$
$ echo $? # 0 indicating no error
0

'''

    