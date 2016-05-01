from packages.aws.sns import SNSObject
from packages.utils.df import Storage
import boto3
import os, sys
from configparser import ConfigParser
import json

'''config.json(config.ini) 설정을 읽어서 특정 storage의 용량을 체크,
    기준값 이상인 경우 push_token_filename을 읽어 push 를 전송한다. 

cat config.json.sample
{
    "storage": {
        "disk_name": Your Storage Name,
        "usage_limit": Your Limit,
        "instance_name": Your instance name,
        "push_token_filename": Your token file name
    }
}

'''
def parse_config():
    config = ConfigParser()
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        with open(file_path, 'r') as config_file:
            config.read(file_path)
            return config
    except IOError as e:
        print("\tconfig.ini not found. try to find config.json...")
        try:
            json_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
            with open(json_file_path) as config_file:
                config = json.loads(config_file.read())
                return config
        except IOError as e:
            print("\tconfig.json file not found...", e)
            return

def check():
    config = parse_config()

    if config != None:
        disk_name = ''
        usage_limit = ''
        instance_name = ''

        if (type(config) == ConfigParser):
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
        else:
            # you can use braces and get function to get value.
            disk_name = config['storage']['disk_name']
            usage_limit = config.get('storage').get('usage_limit')
            instance_name = config.get('storage').get('instance_name')

        print("{}, {}, {}".format(disk_name, usage_limit, instance_name))
        storage = Storage()
        result = storage.check_usage_is_over(disk_name, int(usage_limit))
        print("result: {}".format(result))

        push_token_filename=''
        if result == True:
            try:
                push_token_filename = config['storage']['push_token_filename']
                f = open(os.path.join(os.path.dirname(__file__), push_token_filename), 'r')
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
    else:
        raise ValueError("config.ini 혹은 config.json 이 존재하여야 합니다.")

if __name__ == '__main__':
    check()
