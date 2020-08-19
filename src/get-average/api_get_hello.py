import json
def hello_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps('Hello upwork')
    }
