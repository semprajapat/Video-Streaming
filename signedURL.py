import boto3

"""
If you don't have CLI and therefore AWS Credentials setup , then un-comment the lines below and remove the line above. Add your AWS credentials.
"""
s3 = boto3.client(
   's3',
   aws_access_key_id='AKIAREM4NU7BJI2WRRXV',
   aws_secret_access_key=''
   config = Config(signature_version='s3v4')
)

bucket = "lbf-videos"
key= raw_input("Enter your desired filename/key for this upload: ")

print (" Generating pre-signed url...")

print(s3.generate_presigned_url('put_object', Params={'Bucket':bucket,'Key':key}, ExpiresIn=3600, HttpMethod='PUT'))
