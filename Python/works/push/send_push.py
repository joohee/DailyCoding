import boto3
from sns import SNSObject
import json
import os, sys

def parse_config():
    ''' config.json을 읽어들입니다. 
        파일명은 고정입니다. 

        Exception: 
            IOError - 파일이 없을 경우 발생합니다. 
    '''
    try:
        json_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(json_file_path) as config_file:
            config = json.loads(config_file.read())
            return config
    except IOError as e:
        print("error: ", e)
        return None

def push(section, message):
    ''' section에 해당하는 파일명을 읽고, message를 전송합니다. 
        packages.aws.sns의 SNSObject를 이용하여 전송합니다. 

        Args: 
            section - config.json 에 기록된 filename
            message - 발송할 메세지. json 형식. 

        Exception: 
            config.json이 없을 경우 발생합니다.  

    '''
    config = parse_config()
    if config != None:
        push_token_file = config[section]['push_token_filename']
        f = open(os.path.join(os.path.dirname(__file__), push_token_file), 'r')
        push_tokens = [s.split() for s in f.read().splitlines()]

        client = boto3.client('sns')
        sns = SNSObject()
        for line in push_tokens:
            token = line[0]
            typ = line[1]
            if typ == 'I':
                sns.push_apns(section, client, token, message)
            else:
                sns.push_gcm(section, client, token, message)

    else:
        print("config.json 없습니다.")

if __name__ == "__main__":
    print("usage: push(section, message)")
