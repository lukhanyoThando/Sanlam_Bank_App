# In your services or SNS publisher
import os
import boto3

def publish_to_sns(message: str):
    sns_client = boto3.client(
        'sns',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    
    sns_client.publish(
        TopicArn=os.getenv('SNS_TOPIC_ARN'),
        Message=message
    )
