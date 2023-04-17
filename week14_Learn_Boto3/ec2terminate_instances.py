#  ec2 terminate instances 
# terminate all instances after creating a list of 
import boto3
ec2 = boto3.client("ec2")
x = ec2.describe_instances()
#print(f"What is the format of this raw data? {x.keys()}")
#print(x['Reservations'])
data = x['Reservations']
ec2_list=[] # prepare for an empty list

for instances in data: 
    instance = instances["Instances"]
    #print(instance)
    instanceId = instance[0]["InstanceId"]
    if 'PublicIpAddress' in (list(instance[0].keys())):
        ec2_list.append(instanceId) # create a list of EC2 instances
    # EC2 instance for Cloud9 does not have a keyword 'PublicIpAddress' 
print(ec2_list)
ec2.terminate_instances(
    InstanceIds=ec2_list    
)
'''
['i-095cc4e25bff6ef3d', 'i-0eb63e80b26d11900', 'i-01ff3b5522cb5e2ba']
'''