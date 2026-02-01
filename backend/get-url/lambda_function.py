import boto3
import json
import uuid

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    file_name = body.get('fileName', f"{uuid.uuid4()}.jpg")
    bucket_name = "smart-image-storage-chinmaya"

    url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': file_name, 'ContentType': 'image/*'},
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': json.dumps({'uploadURL': url})
    }