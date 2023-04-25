import boto3

dynamodb = boto3.resource('dynamodb', 
    aws_access_key_id='AKIAXVYQ2OVDZIVL2NX2',
    aws_secret_access_key='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',region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
#        {
#            'AttributeName': 'id',
#            'AttributeType': 'N'
#        },
#        {
#            'AttributeName': 'createdAt',
#            'AttributeType': 'S'
#        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print("Table status:", table.table_status)