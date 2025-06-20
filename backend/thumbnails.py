import boto3
import json
import os

s3 = boto3.client('s3')
THUMBNAIL_BUCKET = os.environ['THUMBNAIL_BUCKET']

def lambda_handler(event, context):
    response = s3.list_objects_v2(Bucket=THUMBNAIL_BUCKET)
    keys = [obj['Key'] for obj in response.get('Contents', [])]

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'images': keys})
    }
