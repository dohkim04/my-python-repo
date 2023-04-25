import boto3

dynamodb = boto3.resource('dynamodb', 
    aws_access_key_id='xxxxxxxxxxxxxxxx',
    aws_secret_access_key='yyyyyyyyyyyyyyyyy',region_name='us-east-1')

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
