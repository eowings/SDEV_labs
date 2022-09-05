import logging
import time
import json
import botocore
from boto3.dynamodb.conditions import Attr, Key
import boto3


def make_table():
    """Create eowings_temp_humid table"""
    dynamodb = boto3.client('dynamodb')
    try:
        dynamodb.create_table(
            TableName='eowings_temp_humid',
            KeySchema=[
                {
                    'AttributeName': 'sample_time',
                    'KeyType': 'HASH'
                },
                {
                'AttributeName': 'device_id',
                'KeyType': 'RANGE'  # Sort key
                }            
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'sample_time',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'device_id',
                    'AttributeType': 'N'
                },                
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except dynamodb.exceptions.ResourceInUseException:
        print("*"*75+"\nTable has already been Created \n"+"*"*75)
        pass


def populate_data():
    """Pull data from eowings_temp_humid.json and populate
    the courses table with it.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eowings_temp_humid')

    # Read the JSON file
    with open("eowings_temp_humid.json") as json_data:
        items = json.load(json_data)

        with table.batch_writer() as batch:
            # Loop through the JSON objects
            for item in items:
                batch.put_item(Item=item)
    
def main():            
    make_table()
    print("Table Has Been Created.")
    time.sleep(15)
    populate_data()
    print("Table Has Been Populated.")
        

main()
    