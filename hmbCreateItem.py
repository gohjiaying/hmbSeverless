import json
import boto3
import random

#define dynamodb item variables
hmb_item_table = "Items"

#define boto variables
dynamodb = boto3.client('dynamodb')


def boto_put_item (table_name, item) :
    response = dynamodb.put_item(
        TableName = table_name,
        Item = item
    )
    return response


def put_shopping_item (item_id, item_name, item_price):
    item = {}
    item['ItemId'] = {"N": item_id}
    item['ItemName'] = {"S": item_name}
    item['Price'] = {"N": item_price}

    response = boto_put_item(hmb_item_table, item)
    return response


def get_item_id ():
    return random.randint(1,999999)


def lambda_handler (event, context):
    # TODO implement
    response = put_shopping_item(get_item_id(), event['name'], event['price'])
    
    return response
