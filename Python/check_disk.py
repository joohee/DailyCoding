from packages.aws.sns import SNSObject
from packages.utils.df import Storage
import boto3
import os, sys
from configparser import ConfigParser

def check():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

    disk_name = ''
    usage_limit = ''
    instance_name = ''

    if config.sections() != None:
        for sec in config.sections():
            try:
                disk_name = config['storage']['disk_name'] 
                usage_limit = config['storage']['usage_limit']
                instance_name = config['storage']['instance_name']
                break
            except KeyError as e:
                print(str(e))
                raise

    print("{}, {}, {}".format(disk_name, usage_limit, instance_name))
    storage = Storage()
    result = storage.check_usage_is_over(disk_name, int(usage_limit))
    print("result: {}".format(result))

    if result == True:
        try:
            f = open('push_tokens.file', 'r')
            push_tokens = [s.split() for s in f.read().splitlines()]

            client = boto3.client('sns')
            sns = SNSObject()
            message_format = '{}의 [{}] 공간 사용량이 {}% 를 초과하였습니다. 체크하시길 바랍니다.'
            message = message_format.format(instance_name, disk_name, usage_limit)

            for line in push_tokens:
                token = line[0]
                typ = line[1]
                if typ == 'I':   
                    sns.push_apns(client, token, message)
                else:
                    sns.push_gcm(client, token, message)
        except:
            raise
    else:
        print("아직 공간이 충분합니다...")

if __name__ == '__main__':
    check()
