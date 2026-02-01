import boto3
import json

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb').Table('ImageReports')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        Features=['GENERAL_LABELS', 'IMAGE_PROPERTIES']
    )
    
    labels = [l['Name'] for l in response['Labels']]
    props = response.get('ImageProperties', {}).get('Quality', {})

    dynamodb.put_item(Item={
        'ImageId': key,
        'Labels': labels,
        'Brightness': str(props.get('Brightness', 0)),
        'Sharpness': str(props.get('Sharpness', 0)),
        'Timestamp': str(event['Records'][0]['eventTime'])
    })
    return {"status": "Analysis Saved"}