
##  configure a lambda funciton and then add trigger in console
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('hello from jerry')
    }
