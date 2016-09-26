import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)




dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


client   = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

try:
    tabledescription = client.describe_table(TableName='Repos')
    #print (tabledescription)
except :
    table = dynamodb.create_table(
        TableName='Repos',
        KeySchema=[
            {
                'AttributeName': 'user',
                'KeyType': 'HASH' #Partition key
            },
            {
                'AttributeName': 'repoName',
                'KeyType': 'RANGE' #Sort key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'repoName',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
        }
    )


Repos =  dynamodb.Table('Repos')

print("Table status:", Repos.table_status)
