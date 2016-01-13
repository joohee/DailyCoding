import boto3
import os
import configparser 
import json

# todo : message invisible in app. check it.
def get_push_message():
    # publish
    dData = {}
    dData['badge'] = 1
    dData['alert'] = 'alert'
    dData['type'] = 'update'
    dGCM = {}
    dGCM['data'] = dData
    dGCM['collapse_key'] = 'Welcome'
    dGCM['delay_while_idle'] = 'true'
    dGCM['time_to_live'] = 125
    dGCM['dry_run'] = 'false'
    message = {}
    message['GCM'] = dGCM
    message['default'] = 'default message'

    try:
        print("*** valud! {}".format(json.dumps(message)))
    except ValueError:
        print("*** invalud!")
        raise

    return message

def get_push_message_apns():
    dData = {}
    dData['badge'] = 1
    dData['alert'] = 'alert'
    dData['type'] = 'update'
    dAPNS = {}
    dAPNS['sound'] = 'default'
    dAPNS['aps'] = dData
    message = {}
    message['APNS'] = dAPNS
    message['default'] = 'default message'

    try:
        print("*** valud! {}".format(json.dumps(message)))
    except ValueError:
        print("*** invalud!")
        raise

    return message

def create_platform_application(client, platform, key, cer):
    apns_attributes = {
        "PlatformCredential": key,
        "PlatformPrincipal": cer
    }
    #print (key_str + "---------")
    #print (cer_str + "---------")
    response = client.create_platform_application(
        Name = 'platformForIOS',
        Platform = platform, 
        Attributes = apns_attributes
    )
    return response

def create_endpoint(client, platformApplicationArn, pushToken):
    platformEndpoint = client.create_platform_endpoint(
        PlatformApplicationArn=platformApplicationArn,
        Token=pushToken,
        CustomUserData='',
        Attributes = {
        }
    )
    return platformEndpoint

def publish(client, endpointArn, message):
    response = client.publish(
        TargetArn=endpointArn,
        Message=json.dumps(message),
        MessageStructure='json'
    )
    return response

def delete_endpoint(client, endpointArn):
    deletedEndpoint = client.delete_endpoint(
        EndpointArn=endpointArn
    )
    return deletedEndpoint

def delete_platform_application(client, platformApplicationArn):
    deletedPlatformApplication = client.delete_platform_application(
        PlatformApplicationArn=platformApplicationArn
    )
    return deletedPlatformApplication

def push_apns(client):

    key_path = os.path.abspath('hotzil_dis_key.pem')
    cer_path = os.path.abspath('hotzil_dis_cer.pem')

    key = open(key_path, 'r')
    cer = open(cer_path, 'r')

    key_str = key.read()
    cer_str = cer.read()

    ### apns
    apns_attributes = {
        "PlatformCredential": key_str,
        "PlatformPrincipal": cer_str
    }
    #print (key_str + "---------")
    #print (cer_str + "---------")
    platform = 'APNS'
    responseAPNS = create_platform_application(client, platform, key_str, cer_str)
    print ("APNS: {}".format(responseAPNS))

    pushToken = input('please insert your pushToken of iOS: ')
    platformApplicationArn = responseAPNS['PlatformApplicationArn']
    platformEndpoint = create_endpoint(client, platformApplicationArn, pushToken)

    endpointArn = platformEndpoint['EndpointArn']
    print ("endpoint: {}".format(endpointArn))

    message = get_push_message_apns()
    response = publish(client, endpointArn, message)
    print ("published: {}".format(response))

    deletedEndpoint = delete_endpoint(client, endpointArn)
    print("delete endpoint: {}".format(deletedEndpoint))

    deletedPlatformApplication = delete_platform_application(client, platformApplicationArn)
    print("delete platform application: {}".format(deletedPlatformApplication))

def push_gcm(client):
    config = configparser.ConfigParser()
    config.read('sns_config.ini')
    server_key = None

    if config.sections() != None:
        try:
            server_key = config.get('sns', 'serverKey')
        except:
            print("there's no serverKey to create GCM application")
            raise

    registrationId = input('please insert your registrationId: ')
    responseGCM = create_platform_application(client, 'GCM', server_key, '')
    print("PlatformApplicationArn: {}".format(responseGCM['PlatformApplicationArn']))

    platform_application_arn = responseGCM['PlatformApplicationArn']
    platformEndpoint = create_endpoint(client, platform_application_arn, registrationId)
    endpointArn = platformEndpoint['EndpointArn']
    print ("endpoint: {}".format(endpointArn))

    message = get_push_message()
    response = publish(client, endpointArn, message)
    print ("published: {}".format(response))

    deletedEndpoint = delete_endpoint(client, endpointArn)
    print("delete endpoint: {}".format(deletedEndpoint))

    deletedPlatformApplication = delete_platform_application(client, platform_application_arn)
    print("delete platform application: {}".format(deletedPlatformApplication))

if __name__ == "__main__":
    client = boto3.client('sns')
    selected = input("please insert your choice: (1 - GCM, 2 - APNS) ")
    if selected == '2':
        push_apns(client)
    else:
        push_gcm(client)
