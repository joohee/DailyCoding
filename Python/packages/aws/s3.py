import boto3
import json

class S3Object:
    '''boto3 모듈을 이용한 s3 access functions.
        - upload(bucket_name, filename, ACL)
            : 특정 버킷/특정 파일을 업로드 합니다. 
              ACL의 default값은 public-read입니다.
        - list(bucket_name, dirname)
            : 특정 버킷 아래 특정 디렉토리의 파일object와 파일 명을 출력합니다. 
        - set_public(object)
            : 특정 s3 object의 ACL을 public-read로 생성합니다. 
        - get_url(bucket_name, key, expiration=3600000, http_method=None)
            : 특정 bucket아래 object의 key에 대해 
              expiration(default 1시간) 만큼 유효한 S3 URL을 리턴합니다. 
              http_method는 제한이 없으며, 특정 method로 제한할 수 있다. 
              (ex. 'GET', 'POST', 'PUT', ...)
    '''

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
