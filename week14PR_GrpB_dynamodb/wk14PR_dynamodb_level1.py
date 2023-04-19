#!/usr/bin/env python3.10
'''
Project B
1. Foundational requirements:
- All code should be inline commented.
- Create a DynamoDB table for something of your choosing (e.g. movies, food, games).
- Using the Gist (https://gist.github.com/zaireali649/0ec6b90155120cf508223788b7b86efc) as a starting point, 
use boto3 and Python to add 10 or more items to the table.
- Use boto3 and Python to scan the DynamoDB table.
- Push your code to GitHub and include the link in your write up.

2. Advanced requirements:
- Use boto3 and Python to query a table, remove an item from a table, create a table, and delete a table.

3. Complex requirements:
- Create a lambda function using boto3 and Python to query a table, 
- return an item from a table and remove/delete an item from a table.
- Run a test of the lambda function to verify you were able to do all of the previous actions.
- Create APIs using API Gateway using the console that will each return query a table, return an item, delete an item by calling your lambda function.
- Note: You can reference the following documentation to point you in the right direction. 
  The code they are using is NOT Python so take that into consideration: 
  https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html
'''
"""
###### Foundation Portion #####
# Guide: execute per each group in turn below:
# Group A: steps 1 and 2: create your new DynamoDB table.
# Group B: steps 3 and 4: add 10 movie items to DynamoDB table
# Group C: step 5       : scan the entire table.
###############################
# First, execute the following Steps 1 and 2. 
# Reference: "Creating a new table" section of the document, https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# [Step1] Connect and get a new DynamoDB service resouce
print("[Step1] Connect and get the DynamoDB service resource")   # Replace the keys below
import boto3 # Get the service resource.
dynamodb = boto3.resource('dynamodb', aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
    aws_secret_access_key='YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY',)
print(f"{dynamodb} is now being created as a DynamoDB resource object.\n") # check if your AWS SDK works properly. 
    # Output: dynamodb.ServiceResource() is now being created as a DynamoDB resource object.
# [Step2] Create a new DynamoDB table, "MyMovieList".
print('[Step2] "MyMovieList" DynamoDB table is being created...\n')
table = dynamodb.create_table(
    TableName = 'MyMovieList',
    AttributeDefinitions=[
        {'AttributeName': 'rank_id','AttributeType': 'N'},{'AttributeName': 'genre',  'AttributeType': 'S'},    
        {'AttributeName': 'title',  'AttributeType': 'S'},{'AttributeName': 'year',   'AttributeType': 'N'},],
    KeySchema = [{'AttributeName': 'rank_id', 'KeyType': 'HASH'},{'AttributeName': 'genre'  ,'KeyType': 'RANGE'},],
    GlobalSecondaryIndexes=[{'IndexName': 'new_search',
        'KeySchema': [{'AttributeName': 'year', 'KeyType': 'HASH'},{'AttributeName': 'title','KeyType': 'RANGE'},],
        'Projection': {'ProjectionType': 'INCLUDE', 'NonKeyAttributes': ['rank_id','genre']},
        'ProvisionedThroughput':{'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},}],    
    ProvisionedThroughput={'ReadCapacityUnits': 5,'WriteCapacityUnits': 5},
    Tags=[{'Key': 'Project 9', 'Value': 'Group B - DynamoDB project'},],
)
table.wait_until_exists() # Wait until the table exists.
print(f"The date and time of creating this table: {table.creation_date_time}")
print(f"The count of items in the table is: {table.item_count}")   # Print the counting number of items
print(f"The table is created as:\n {table}")
print("===============\n")
"""
# The output is below:
# [Step1] Connect and get the DynamoDB service resource
# dynamodb.ServiceResource() is now being created as a DynamoDB resource object.
#
# [Step2] "MyMovieList" DynamoDB table is being created...
#
# The date and time of creating this table: 2023-04-18 12:52:59.224000-04:00
# The count of items in the table is: 0
# The table is created as:
#  dynamodb.Table(name='MyMovieList')
# ===============
# 
# []
#####
'''
# [Step3] Read each item from 'movie_table.csv' file, and Create a list of movie dictionaries.
import csv             # import a 'cvs' Python library to access to CSV files.
entire_movie_list=[]   # Initialize as an empty list.
eachRow=[]             # eachRow list will consist of 3 items; Rank_ID, Title, and Year.
with open('movie_table.csv', newline='') as csvfile:    # open movie_table.csv file and read by each entire new line, 
                                                        # then designate it as an csvfile object.
    fileReader = csv.reader(csvfile, delimiter= ",", quotechar = None)  # See comma delimiter as a separator 
                                                                        # to recognize individual items
    for eachRow in fileReader:  # eachRow is assigned to each new line  
        Item={}                 # Reinitizlie as empty dictionary per each new line
        # Add 3 individual items per each movie below:
        Item['rank_id'] = int(eachRow[0])
        Item['genre'] = eachRow[1]
        Item['title'] = eachRow[2]
        Item['year'] = int(eachRow[3])
        entire_movie_list.append(Item) # Add each movie dictionary to the entire movie list
    print(f"The following movie list will be added to MyMovieList table:\n{entire_movie_list}")
# [Step 4] add 10 or more itmes to the table after call the DynamoDB table. 
import boto3
dynamodb = boto3.resource('dynamodb') # Get the service resource.
table = dynamodb.Table('MyMovieList') # call your MyMovieList DynamoDB table
# add a list of 10 movie dictionaries to MyMovieList DynamoDB table.
for i in range(len(entire_movie_list)):
    table.put_item(Item=entire_movie_list[i])
print("Completed to add all your movie dictionaries to your DynamoDB table...")
print(f"The number of your table items: {table.item_count}")
print(f"The entire table below:\n{table}")
'''
#####
""" The Output is shown below:
The following movie list will be added to MyMovieList table:
[{'rank_id': 2, 'genre': 'Drama', 'title': 'The God Father', 'year': 1972},
 {'rank_id': 6, 'genre': 'Romance', 'title': 'Gone with the Wind', 'year': 1939},
 {'rank_id': 8, 'genre': 'Drama', 'title': " Schindler's List", 'year': 1993},
 {'rank_id': 10, 'genre': 'Musical', 'title': ' The Wizard of Oz', 'year': 1939}, 
 {'rank_id': 15, 'genre': 'Adventure', 'title': 'Star Wars', 'year': 1977}, 
 {'rank_id': 40, 'genre': 'Musical', 'title': 'The Sound of Music', 'year': 1965}, 
 {'rank_id': 41, 'genre': 'Adventure', 'title': 'King Kong', 'year': 1933}, 
 {'rank_id': 57, 'genre': 'Drama', 'title': 'Rocky', 'year': 1976}, 
 {'rank_id': 74, 'genre': 'Drama', 'title': 'The Silence of the Lambs', 'year': 1991}, 
 {'rank_id': 100, 'genre': 'Epic', 'title': 'Ben-Hur', 'year': 1959}]
Completed to add all your movie dictionaries to your DynamoDB table...
The number of your table items: 0
The entire table below:
dynamodb.Table(name='MyMovieList')

"""

#########################################################
#'''
# [Step 5] Scan the DynamoDB table
    # KeySchema = [{'AttributeName': 'rank_id', 'KeyType': 'HASH'},{'AttributeName': 'genre'  ,'KeyType': 'RANGE'},],
import boto3
from boto3.dynamodb.conditions import Key, Attr
#dynamodb = boto3.resource('dynamodb') # Get the service client. 
# AttributeError: 'dynamodb.ServiceResource' object has no attribute 'scan'
dynamodb = boto3.client('dynamodb')
#table = dynamodb.Table('MyMovieList') # call your MyMovieList DynamoDB table
response = dynamodb.scan(
#    ExpressionAttributeNames={
#        '#RI':'rank_id', '#G': 'genre', '#T': 'title', '#Y': 'year'},
#    ExpressionAttributeValues={
#        :alldrama': {'S': 'Drama',}, 
#    },
#    FilterExpression='genre = :alldrama',
#    ProjectionExpression='#RI, #G, #T, #Y',     
    TableName = 'MyMovieList'
)
print(f"a raw data of this table is:\n{response}")
print()
items = response['Items']
print(f"a list of items on this table is:\n{items}")
#'''
#####

"""Note: the following output format was slightly rearranged for indentation for better visualization.
a raw data of this table is:
{'Items': [{'rank_id': {'N': '8'}, 'year': {'N': '1993'}, 'genre': {'S': 'Drama'}, 'title': {'S': " Schindler's List"}}, 
           {'rank_id': {'N': '10'}, 'year': {'N': '1939'}, 'genre': {'S': 'Musical'}, 'title': {'S': ' The Wizard of Oz'}}, 
           {'rank_id': {'N': '2'}, 'year': {'N': '1972'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'The God Father'}},
           {'rank_id': {'N': '40'}, 'year': {'N': '1965'}, 'genre': {'S': 'Musical'}, 'title': {'S': 'The Sound of Music'}},
           {'rank_id': {'N': '100'}, 'year': {'N': '1959'}, 'genre': {'S': 'Epic'}, 'title': {'S': 'Ben-Hur'}},
           {'rank_id': {'N': '41'}, 'year': {'N': '1933'}, 'genre': {'S': 'Adventure'}, 'title': {'S': 'King Kong'}},
           {'rank_id': {'N': '6'}, 'year': {'N': '1939'}, 'genre': {'S': 'Romance'}, 'title': {'S': 'Gone with the Wind'}},
           {'rank_id': {'N': '15'}, 'year': {'N': '1977'}, 'genre': {'S': 'Adventure'}, 'title': {'S': 'Star Wars'}},
           {'rank_id': {'N': '57'}, 'year': {'N': '1976'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'Rocky'}},
           {'rank_id': {'N': '74'}, 'year': {'N': '1991'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'The Silence of the Lambs'}}],
 'Count': 10, 'ScannedCount': 10, 
 'ResponseMetadata': {'RequestId': '915FDBK650Q7F8A836K24033TJVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 
                      'HTTPHeaders': {'server': 'Server', 'date': 'Tue, 18 Apr 2023 17:24:56 GMT', 
                      'content-type': 'application/x-amz-json-1.0', 'content-length': '1009', 'connection': 'keep-alive', 
                      'x-amzn-requestid': '915FDBK650Q7F8A836K24033TJVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3013873324'}, 
 'RetryAttempts': 0}
}

a list of items on MyMovieList DynamoDB table is:
[{'rank_id': {'N': '8'}, 'year': {'N': '1993'}, 'genre': {'S': 'Drama'}, 'title': {'S': " Schindler's List"}}, 
 {'rank_id': {'N': '10'}, 'year': {'N': '1939'}, 'genre': {'S': 'Musical'}, 'title': {'S': ' The Wizard of Oz'}}, 
 {'rank_id': {'N': '2'}, 'year': {'N': '1972'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'The God Father'}},
 {'rank_id': {'N': '40'}, 'year': {'N': '1965'}, 'genre': {'S': 'Musical'}, 'title': {'S': 'The Sound of Music'}},
 {'rank_id': {'N': '100'}, 'year': {'N': '1959'}, 'genre': {'S': 'Epic'}, 'title': {'S': 'Ben-Hur'}},
 {'rank_id': {'N': '41'}, 'year': {'N': '1933'}, 'genre': {'S': 'Adventure'}, 'title': {'S': 'King Kong'}},
 {'rank_id': {'N': '6'}, 'year': {'N': '1939'}, 'genre': {'S': 'Romance'}, 'title': {'S': 'Gone with the Wind'}},
 {'rank_id': {'N': '15'}, 'year': {'N': '1977'}, 'genre': {'S': 'Adventure'}, 'title': {'S': 'Star Wars'}},
 {'rank_id': {'N': '57'}, 'year': {'N': '1976'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'Rocky'}},
 {'rank_id': {'N': '74'}, 'year': {'N': '1991'}, 'genre': {'S': 'Drama'}, 'title': {'S': 'The Silence of the Lambs'}}],
"""

###############

"""
##### Retrieve individual dictionaries representing each movie item using Scan method ####
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 
# boto3.client('dynamodb', region_name='us-east-1') causes AttributeError: 'DynamoDB' object has no attribute 'Table'
table = dynamodb.Table('MyMovieList') # retrieve table object of MyMovieList DynamoDB table.

## Retrieve each dictionary per each movie from the DynamoDB table.
response = table.scan()   # Receive an entire table data as response object for scanning. 
items = response['Items'] # Retrieve a single "items" list that corresponds to "Item" Key in the response.
for each_item in items:   # Iterate each dictionary present within the list per loop.
    print(each_item)      # print each_item, a dictionary per each movie item.
"""
'''Output below:
dohyungkim2023@DESKTOP-82B8HN7:~/my-python-repo/week14PR_GrpB_dynamodb$ python3 wk14PR_dynamodb.py
{'rank_id': Decimal('8'), 'year': Decimal('1993'), 'genre': 'Drama', 'title': " Schindler's List"}
{'rank_id': Decimal('10'), 'year': Decimal('1939'), 'genre': 'Musical', 'title': ' The Wizard of Oz'}
{'rank_id': Decimal('2'), 'year': Decimal('1972'), 'genre': 'Drama', 'title': 'The God Father'}
{'rank_id': Decimal('40'), 'year': Decimal('1965'), 'genre': 'Musical', 'title': 'The Sound of Music'}
{'rank_id': Decimal('100'), 'year': Decimal('1959'), 'genre': 'Epic', 'title': 'Ben-Hur'}
{'rank_id': Decimal('41'), 'year': Decimal('1933'), 'genre': 'Adventure', 'title': 'King Kong'}
{'rank_id': Decimal('6'), 'year': Decimal('1939'), 'genre': 'Romance', 'title': 'Gone with the Wind'}
{'rank_id': Decimal('15'), 'year': Decimal('1977'), 'genre': 'Adventure', 'title': 'Star Wars'}
{'rank_id': Decimal('57'), 'year': Decimal('1976'), 'genre': 'Drama', 'title': 'Rocky'}
{'rank_id': Decimal('74'), 'year': Decimal('1991'), 'genre': 'Drama', 'title': 'The Silence of the Lambs'}
'''