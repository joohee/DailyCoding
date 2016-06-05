import boto3
from sns import SNSObject
import json
import os, sys
import random
import send_push

'''
    send_push 모듈을 테스트 하기 위한 파일입니다.
    
    TODO:
        uniitest 로 변경해보기.

'''
if __name__ == "__main__":
    messages = ('test message1', 'test message2', 'test message3')
    rand = random.randrange(0, len(messages))
    send_push.push('section', messages[rand])
