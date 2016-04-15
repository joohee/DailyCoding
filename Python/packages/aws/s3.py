import boto3
import json

class S3Object:

    def __init__(self, profile_name):
        self.session = boto3.Session(profile_name=profile_name)
        self.s3 = self.session.resource('s3')
        for bucket in self.s3.buckets.all():
            print(bucket.name)
        pass

    def upload(self, bucket_name, filename, ACL='public-read'):
        data = open(filename, 'rb')
        self.s3.Bucket(bucket_name).put_object(Key=filename, Body=data, ACL=ACL)

    def list(self, bucket_name, dirname):
        fileobjs = []
        filenames = []
        bucket = self.s3.Bucket(bucket_name)
        for key in bucket.objects.all():
            if key.key.startswith(dirname):
                fileobjs.append(key)
                filenames.append(key.key)
                #print(key.key)
        return fileobjs, filenames
    
    def set_public(self, obj):
        obj.Acl().put(ACL='public-read')
        print("{} set be public...".format(obj.key))

    def get_url(self, bucket_name, key, expiration=3600000, http_method=None):
        params = {}
        params['Bucket'] = bucket_name
        params['Key'] = key
        url = self.client.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration, HttpMethod=http_method)

        print (url)
        return url

if __name__ == '__main__':
    print("use S3Object class")
