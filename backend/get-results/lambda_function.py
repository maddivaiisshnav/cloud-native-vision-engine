import boto3
import json

dynamodb = boto3.resource('dynamodb').Table('ImageReports')

def lambda_handler(event, context):
    image_id = event.get('queryStringParameters', {}).get('imageId')
    response = dynamodb.get_item(Key={'ImageId': image_id})
    item = response.get('Item', {})

    return {
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': json.dumps(item)
    }