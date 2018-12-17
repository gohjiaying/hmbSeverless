import json
import boto3
import os

#define dynamodb item variables
hmb_request_item_table = os.environ['REQUEST_TABLE']

#define boto variables
dynamodb = boto3.client('dynamodb')


def get_request_items ():
    response = boto_scan(hmb_item_table)
    return response


def boto_scan (table_name) :
    response = dynamodb.scan(
        TableName = table_name,
        FilterExpression = "Quantity = :val",
        ExpressionAttributeValues = {":val": {"N": str(0)}}
    )
    return response


def lambda_function (event, context):
    result = get_request_items()
    print(response)
    
    to_return = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }
    return to_return
