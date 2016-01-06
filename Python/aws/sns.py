import boto3
import os
import configparser 

key_path = os.path.abspath('apns_dis_key.pem')
cer_path = os.path.abspath('apns_dis_cer.pem')

key = open(key_path, 'r')
cer = open(cer_path, 'r')

key_str = key.read()
cer_str = cer.read()

client = boto3.client('sns')


config = configparser.ConfigParser()
config.read('sns_config.ini')
server_key = None

if config.sections() != None:
    try:
        server_key = config.get('sns', 'serverKey')
    except:
        print("there's no serverKey to create GCM application")
        raise

responseGCM = client.create_platform_application(
    Name = "pythontest",
    Platform = "GCM", 
    Attributes = {
        "PlatformCredential": server_key,
        "PlatformPrincipal": ""
    }
)
print(responseGCM)

apns_attributes = {
        "PlatformPrincipal": cer_str,
        "PlatformCredential": key_str
}
print (cer_str + "---------")
print (key_str + "---------")
responseAPNS = client.create_platform_application(
    Name = 'pythontest',
    Platform = 'APNS',
    Attributes = apns_attributes 
)

print (response)
