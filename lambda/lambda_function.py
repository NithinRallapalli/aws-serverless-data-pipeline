import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersData')

def lambda_handler(event, context):
    try:
        city = None

        if event.get('queryStringParameters'):
            city = event['queryStringParameters'].get('city')

        if city:
            response = table.scan(
                FilterExpression="city = :c",
                ExpressionAttributeValues={":c": city}
            )
        else:
            response = table.scan()

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
