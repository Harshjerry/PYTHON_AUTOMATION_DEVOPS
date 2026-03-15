import boto3
client = boto3.client('s3')
response = client.create_bucket(
    Bucket='demo_harsh_boto3_bucket'
)

#this will create a bucket directly in your  console and  configured region 
