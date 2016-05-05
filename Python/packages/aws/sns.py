import boto3
import os
import configparser 
import json

class SNSObject:
    """ Amazon SNS 모듈을 이용하여 Push Notification을 전송합니다. 

        도움말을 html로 저장하려면 아래 명령어를 입력하세요.
            pydoc -w sns

    """

    def __init__(self):
        """ 사용할 SNS 클라이언트는 계속 활용되므로 class 내부 변수로 생성합니다. 
            default message는 호출한 쪽에서 메세지를 입력하지 않았을 때 사용합니다.  
        """
        self.client = boto3.client('sns')
        self.default_message = 'default message'

    # todo : message invisible in app. check it.
    def get_push_message_gcm(self, msg):
        """ GCM 포맷에 맞는 message를 JSON 타입으로 변환하여 리턴합니다. 
        """
        text = msg if msg != None else self.default_message
        # publish
        dData = {}
        dData['badge'] = 1
        dData['alert'] = text
        dData['type'] = 'update'
        dGCM = {}
        dGCM['data'] = dData
        dGCM['collapse_key'] = 'Welcome'
        dGCM['delay_while_idle'] = 'true'
        dGCM['time_to_live'] = 125
        dGCM['dry_run'] = 'false'
        message = {}
        message['GCM'] = json.dumps(dGCM)
        message['default'] = 'default message'
    
        try:
            print("*** valid! {}".format(json.dumps(message)))
        except ValueError:
            print("*** invalid!")
            return
    
        return message

    def get_push_message_apns(self, msg):
        """ APNS 포맷에 맞는 message를 JSON 타입으로 변환하여 리턴합니다. 
        """
        text = msg if msg != None else self.default_message

        message = {}
        message['default'] = self.default_message
    
        dData = {}
        dData['badge'] = 1
        dData['alert'] = text
        dData['type'] = 'update'
        dData['sound'] = 'default'
        dAPNS = {}
        dAPNS['aps'] = dData
        message['APNS'] = json.dumps(dAPNS)
    
        try:
            print("*** valid! {}".format(json.dumps(message)))
        except ValueError:
            print("*** invalid!")
            return
    
        return message
    
    def create_platform_application(self, client, platform, key, cer):
        """ Push를 발송할 수 있는 어플리케이션을 생성합니다. 
          이때 APNS는 Push인증서로 생성한 cer/key 파일이, GCM은 Google에서 발급한 serverKey값이 필요합니다. 
        """
        apns_attributes = {
            "PlatformCredential": key,
            "PlatformPrincipal": cer
        }
        #print (key_str + "---------")
        #print (cer_str + "---------")
        response = client.create_platform_application(
            Name = 'platformForPython',
            Platform = platform, 
            Attributes = apns_attributes
        )
        return response
    
    def create_endpoint(self, client, platformApplicationArn, pushToken):
        """ 생성한 platformApplication과 GCM.registraionId 혹은 APNS.pushToken을 이용하여 
          Push를 전송할 endpoint를 생성하는 메소드입니다. 
        """
        platformEndpoint = client.create_platform_endpoint(
            PlatformApplicationArn=platformApplicationArn,
            Token=pushToken,
            CustomUserData='',
            Attributes = {
            }
        )
        return platformEndpoint
    
    def publish(self, client, endpointArn, message):
        """ endpoint로 메세지를 전송하는 역할을 담당합니다.
        """
        response = client.publish(
            MessageStructure='json',
            Message=json.dumps(message),
            TargetArn=endpointArn
        )
        return response
    
    def delete_endpoint(self, client, endpointArn):
        """ 위에서 생성한 endpoint를 삭제합니다. 
        """
        deletedEndpoint = client.delete_endpoint(
            EndpointArn=endpointArn
        )
        return deletedEndpoint
    
    def delete_platform_application(self, client, platformApplicationArn):
        """ 위에서 생성한 platformApplication을 삭제합니다. 
        """
        deletedPlatformApplication = client.delete_platform_application(
            PlatformApplicationArn=platformApplicationArn
        )
        return deletedPlatformApplication

    def push_apns(self, client, pushToken, message=None):
        """ APNS 플랫폼에 따라 push를 전송하는 메소드입니다. 
          message는JSON 포맷으로 이루어지며,  
          get_push_message_gcm, get_push_message_apns를 통해 
          플랫폼에 맞는 JSON 형식으로 리턴됩니다. 
        """
        key_str, cer_str, key_filename, cer_filename=('',)*4

        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'sns_config.ini')))
    
        if config.sections() != None:
            try:
                key_filename = config.get('sns', 'apns_key_filename')
                cer_filename = config.get('sns', 'apns_cer_filename') 
            except:
                print("there's no filename to push notification.")
                return
        else:
            print("check your config...")
            return

        try:
            dir_name = os.path.dirname(__file__)
            key_path = os.path.abspath(os.path.join(dir_name, key_filename))
            cer_path = os.path.abspath(os.path.join(dir_name, cer_filename))
    
            key = open(key_path, 'r')
            cer = open(cer_path, 'r')
    
            key_str = key.read()
            cer_str = cer.read()
    
            if key_str == '' or cer_str == '':
                print('key file or cer file is invalid...')
                return 
    
        except FileNotFoundError:
            print("please check if file is exist")
            return
    
        ### apns
        apns_attributes = {
            "PlatformCredential": key_str,
            "PlatformPrincipal": cer_str
        }
        #print (key_str + "---------")
        #print (cer_str + "---------")
    
        platform = 'APNS'
        responseAPNS = self.create_platform_application(client, platform, key_str, cer_str)
        print ("APNS: {}".format(responseAPNS))
    
        platformApplicationArn = responseAPNS['PlatformApplicationArn']
        platformEndpoint = self.create_endpoint(client, platformApplicationArn, pushToken)
    
        endpointArn = platformEndpoint['EndpointArn']
        print ("endpoint: {}".format(endpointArn))
    
        msg = self.get_push_message_apns(message)
        response = self.publish(client, endpointArn, msg)
        print ("published: {}".format(response))
    
        deletedEndpoint = self.delete_endpoint(client, endpointArn)
        print("delete endpoint: {}".format(deletedEndpoint))
    
        deletedPlatformApplication = self.delete_platform_application(client, platformApplicationArn)
        print("delete platform application: {}".format(deletedPlatformApplication))
    
    def push_gcm(self, client, registrationId, message=None):
        """
          GCM 플랫폼에 따라 push를 전송하는 메소드입니다. 
          message는JSON 포맷으로 이루어지며,  
          get_push_message_gcm, get_push_message_apns를 통해 
          플랫폼에 맞는 JSON 형식으로 리턴됩니다. 
        """
    
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'sns_config.ini')))
        server_key = None
    
        if config.sections() != None:
            try:
                server_key = config.get('sns', 'serverKey')
                print("serverKey: {}".format(server_key))
            except:
                print("there's no serverKey to create GCM application")
                return
    
        responseGCM = self.create_platform_application(client, 'GCM', server_key, '')
        print("PlatformApplicationArn: {}".format(responseGCM['PlatformApplicationArn']))
    
        platform_application_arn = responseGCM['PlatformApplicationArn']
        platformEndpoint = self.create_endpoint(client, platform_application_arn, registrationId)
        endpointArn = platformEndpoint['EndpointArn']
        print ("endpoint: {}".format(endpointArn))
    
        msg = self.get_push_message_gcm(message)
        response = self.publish(client, endpointArn, msg)
        print ("published: {}".format(response))
    
        deletedEndpoint = self.delete_endpoint(client, endpointArn)
        print("delete endpoint: {}".format(deletedEndpoint))

        deletedPlatformApplication = self.delete_platform_application(client, platform_application_arn)
        print("delete platform application: {}".format(deletedPlatformApplication))

if __name__ == "__main__":
    sns = SNSObject()
    client = boto3.client('sns')
    selected = input("please insert your choice: (1 - GCM, 2 - APNS) ")
    pushToken = input('please insert your pushToken: ')
    message = input('please insert message. if you don\'t insert it, you\'ll get the default message: ')

    if selected == '2':
        if len(message) > 0:
            sns.push_apns(client, pushToken, message)
        else:
            sns.push_apns(client, pushToken)
    else:
        if len(message) > 0:
            sns.push_gcm(client, pushToken, message)
        else:
            sns.push_gcm(client, pushToken)
