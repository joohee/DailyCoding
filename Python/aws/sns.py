import boto3
import os
import configparser 
import json

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
    Name = "platformForGCM",
    Platform = "GCM", 
    Attributes = {
        "PlatformCredential": server_key,
        "PlatformPrincipal": ""
    }
)
print(responseGCM)
print("PlatformApplicationArn: {}".format(responseGCM['PlatformApplicationArn']))

platform_application_arn = responseGCM['PlatformApplicationArn']

registrationId='cZ31Jt3jUOk:APA91bEwJc_NZx0ol1XWCXl-lIRih1hYGgdtBpyDQsxmB-vAM812ETuQOawsDVHQH0Osp9lIWhwbdWMakp6FnsNRZIPvhDauEvmyQ0PGT1-8oPRXzHPvSkJAgxAI751DvILPfx3QuN0N'

platformEndpoint = client.create_platform_endpoint(
        PlatformApplicationArn=platform_application_arn,
        Token=registrationId,
        CustomUserData='',
        Attributes = {
        }
)

print(platformEndpoint)
endpointArn = platformEndpoint['EndpointArn']
print ("endpoint: {}".format(endpointArn))

#message = '{GCM:{"collapse_key":"Welcome","data":{"badge":"3","alert":"[Hotzil] message","type":"update"},"delay_while_idle":"true","time_to_live":"125","dry_run":"false"}}'
#message = '{GCM:{"collapse_key":"Welcome","data":{"badge":"3","alert":"[Hotzil] message","type":"update"},"delay_while_idle":"true","time_to_live":"125","dry_run":"false"}}'
#message = {GCM:{collapse_key:Welcome,data:{badge:3,alert:\'[Hotzil] message\',type:update},delay_while_idle:true,time_to_live:125,dry_run:false}}
message = '{"GCM":"{\"collapse_key\":\"Welcome\",\"data\":{\"badge\":3,\"alert\":\"[Hotzil] message\",\"type\":\"update\"},\"delay_while_idle\":true,\"time_to_live\":125,\"dry_run\":false}"}'

response = client.publish(
        TargetArn=endpointArn,
        #Message=json.loads(message),
        Message=message,
        MessageStructure='json'
)

print (response)

client.delete_endpoint(
        endpointArn=endpointArn
        )




### apns
apns_attributes = {
        "PlatformCredential": key_str,
        "PlatformPrincipal": cer_str
}
#print (key_str + "---------")
#print (cer_str + "---------")
responseAPNS = client.create_platform_application(
    Name = 'platformForIOS',
    Platform = 'APNS',
    Attributes = apns_attributes 
)

print (response)
