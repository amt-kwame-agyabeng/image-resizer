import json
import boto3
import urllib.parse
import os

s3 = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    query = event['queryStringParameters']
    file_name = urllib.parse.unquote(query['name'])
    file_type = query['type']

    presigned_url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': BUCKET_NAME,
            'Key': file_name,
            'ContentType': file_type
        },
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'uploadUrl': presigned_url})
    }
