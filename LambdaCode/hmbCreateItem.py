import json
import boto3
import random
import logging
import os

#define dynamodb item variables
hmb_item_table = os.environ['ITEMS_TABLE']
hmb_item_table_required_field = os.environ['ITEMS_TABLE_REQUIRED_FIELDS']

#define boto variables
dynamodb = boto3.client('dynamodb')


def generate_item_id ():
    return random.randint(1,999999)
    
    
def is_valid_shopping_data (data) :
    for field in hmb_item_table_required_field:
        if field not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't create the shopping item.")
            return
        
        
def put_shopping_item (item_id, item_name, item_price):
    item = {}
    item['ItemId'] = {"N": item_id}
    item['ItemName'] = {"S": item_name}
    item['Price'] = {"N": item_price}

    response = boto_put_item(hmb_item_table, item)
    return response


def boto_put_item (table_name, item) :
    response = dynamodb.put_item(
        TableName = table_name,
        Item = item
    )
    return response


def create_item (event, context):
    # TODO implement
    data = json.loads(event['body'])
    response = put_shopping_item(str(generate_item_id()), data['name'], data['price'])
    print(response)
    
    to_return = {
        "statusCode": 200,
        "body": json.dumps(data)
    }

    return to_return
