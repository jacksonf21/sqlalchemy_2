import boto3
client = boto3.client('s3', region_name='us-west-1')

def upload(bucket, file, remote_name):
    client.upload_file(file, bucket, remote_name)

# upload('split-wise-receipts-lhl', 'new-image.png')