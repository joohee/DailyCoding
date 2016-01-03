import boto3
import os

key_path = os.path.abspath('apns_dis_key.pem')
cer_path = os.path.abspath('apns_dis_cer.pem')

key = open(key_path, 'r')
cer = open(cer_path, 'r')

key_str = key.read()
cer_str = cer.read()

client = boto3.client('sns')

#print (key_str + "---------")
#print (cer_str + "---------")

responseGCM = client.create_platform_application(
    Name = "pythontest",
    Platform = "GCM", 
    Attributes = {
        "PlatformCredential": "your server key",
        "PlatformPrincipal": ""
    }
)
print(responseGCM)

responseAPNS = client.create_platform_application(
    Name = 'pythontest',
    Platform = 'APNS',
    Attributes = {
        "PlatformPrincipal": cer_content,
        "PlatformCredential": key_content
})

print (response)
