import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersData')

def lambda_handler(event, context):
    try:
        # Get all users from DynamoDB
        response = table.scan()

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response['Items'])
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
