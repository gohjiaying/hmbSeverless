import json
import boto3
import logging
import os

#define dynamodb request variables
hmb_request_table = os.environ['REQUEST_TABLE']
hmb_request_table_required_field = ['item', 'user']

#define boto variables
dynamodb = boto3.client('dynamodb')


def is_valid_request (data) :
    for field in hmb_request_table_required_field:
        print(field)
        if field not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't create the request item.")
            return
    return True
        

def create_request (data):
    key = {}
    key['Item'] = {"S": data['item']}
    key['User'] = {"S": data['user']}

    if "quantity" not in data:
        quantity = 1
    else:
        quantity =  data["quantity"]

    update_expression = "ADD Quantity :q"
    expression_attribute_values = {}
    expression_attribute_values[':q'] = {"N": str(quantity)}
    response = boto_update_item(hmb_request_table, key, update_expression, expression_attribute_values)
    return response


def boto_update_item (table_name, key, update_expression,expression_attribute_values) :
    response = dynamodb.update_item(
        TableName = table_name,
        Key = key,
        UpdateExpression = update_expression,
        ExpressionAttributeValues = expression_attribute_values
    )
    return response


def lambda_handler (event, context):
    # TODO implement
    data = json.loads(event['body'])
    if is_valid_request(data):
        response = create_request(data)
        print(response)
    
        to_return = {
            "statusCode": 200,
            "body": json.dumps(data)
        }

        return to_return
    else:
        raise Exception("Something went wrong")
        return
