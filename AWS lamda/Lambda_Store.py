import boto3
from botocore.exceptions import NoCredentialsError


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Extracting the file from the event
    file = event.get('file')
    file_name = file['name']
    file_content = file['content']
    bucket_name = 'your-s3-bucket-name'


    try:
        # Uploading the file to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'  # You can adjust the ContentType accordingly
        )
        return {
            'statusCode': 200,
            'body': {
                'message': f'{file_name} uploaded successfully!'
            }
        }
    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': {
                'message': 'Credentials not available!'
            }
        }