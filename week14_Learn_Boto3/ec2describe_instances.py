#  ec2 describe instances
import boto3
ec2 = boto3.client("ec2")
x = ec2.describe_instances()
print(f"What is the format of this raw data? {x.keys()}")
#print(x['Reservations'])
print(f"The size of x['Reservations'] is {len(x['Reservations'])}") # 3 Instance IDs are present
data = x['Reservations']

for i in range(len(data)): # use len() to make 
    data_instance = data[i] # find each component from the list.
    #print(data_instance)   # each component is a dictionary
    print(data_instance.keys()) # all the keys are presented per each data_instance. 
    print(data_instance["Instances"][0]['InstanceId']) 
    # Using "Instances" key, retrieve only one single list.
    # The single list also contains only one single dictionary, so use index 0 to retrieve the dictionary.
    # Find the value corresponding to "InstanceId" key within the single dictionary. 






'''
What is the format of this raw data? dict_keys(['Reservations', 'ResponseMetadata'])
The size of x['Reservations'] is 3
dict_keys(['Groups', 'Instances', 'OwnerId', 'ReservationId'])
i-095cc4e25bff6ef3d
dict_keys(['Groups', 'Instances', 'OwnerId', 'RequesterId', 'ReservationId'])
i-0082f23e1a94d3013
dict_keys(['Groups', 'Instances', 'OwnerId', 'ReservationId'])
i-01ff3b5522cb5e2ba
'''