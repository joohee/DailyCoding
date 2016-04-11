import boto3
import json

class S3Object:

    def __init__(self, profile_name):
        self.session = boto3.Session(profile_name=profile_name)
        self.s3 = self.session.resource('s3')
        for bucket in self.s3.buckets.all():
            print(bucket.name)
        pass

    def upload(self, bucket_name, filename):
        data = open(filename, 'rb')
        self.s3.Bucket(bucket_name).put_object(Key=filename, Body=data)

if __name__ == '__main__':
    s3 = S3Object('profile_name')
    s3.upload('test-bucket', 'test_file.txt')
