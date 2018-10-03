import boto3

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
#new_bucket = s3.create_bucket(Bucket='automatingawsuseast2carstenclaussen',
#    CreateBucketConfiguration={'LocationConstraint':'EU'}
#    )
# for bucket in s3.buckets.all():
#     print(bucket)

# ec2_client = session.client('ec2')
# ec2_client.allocate_address
