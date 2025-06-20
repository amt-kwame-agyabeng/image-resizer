import json
import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get S3 event details
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    # Define target bucket
    target_bucket = "photo-sharing-thumbnails-dev"
    target_key = f"thumb-{source_key}"

    # Download the original image
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image_data = response['Body'].read()
    image = Image.open(io.BytesIO(image_data))

    # Detect original image format before any transformation
    format = (image.format or 'JPEG').upper()

    # Resize the image
    image.thumbnail((150, 150))

    # Handle transparency for formats with alpha channel
    if image.mode in ("RGBA", "LA"):
        background = Image.new("RGBA", image.size, (255, 255, 255, 0))
        background.paste(image, mask=image.split()[-1])
        image = background

    # Map format to content type
    content_type_map = {
        'JPEG': 'image/jpeg',
        'PNG': 'image/png',
        'WEBP': 'image/webp',
        'GIF': 'image/gif'
    }
    content_type = content_type_map.get(format, 'image/jpeg')

    # Save resized image to buffer
    buffer = io.BytesIO()
    image.save(buffer, format)
    buffer.seek(0)

    # Upload thumbnail
    s3.put_object(
        Bucket=target_bucket,
        Key=target_key,
        Body=buffer,
        ContentType=content_type
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Thumbnail created: {target_key}')
    }
