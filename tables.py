# reference: http://boto3.readthedocs.io/en/latest/guide/dynamodb.html

import boto3

dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='student',
    KeySchema=[
        {
            'AttributeName': 'studentID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'studentID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#prints the count of rows
print(table.item_count)


# putting the data in batch format

with table.batch_writer() as batch:
    batch.put_item(
        Item={
		
            'studentID':  1,
            'first_name': 'Amar',
            'last_name': 'Adam',
            'age': 25,
            'address': {
                'road': '1 Jefferson Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zipcode': 90001
            }
        }
    )
    batch.put_item(
        Item={
            'studentID':  2,
            'first_name': 'Judy',
            'last_name': 'James',
            'age': 40,
            'address': {
                'road': '2 Washington Avenue',
                'city': 'Seattle',
                'state': 'WA',
                'zipcode': 98109
            }
        }
    )
    batch.put_item(
        Item={
            'studentID':  3,
            'first_name': 'Alice',
            'last_name':  'Smith',
            'age': 18,
            'address': {
                'road': '3 Madison Lane',
                'city': 'Louisville',
                'state': 'KY',
                'zipcode': 40213
            }
        }
    )
    batch.put_item(
        Item={
            'studentID':  4,
            'first_name': 'Alice',
            'last_name': 'Doe',
            'age': 27,
            'address': {
                'road': '1 Jefferson Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zipcode': 90001
            }
        }
    )
	
	# Delete the tables;
	 # table.delete()
	
	