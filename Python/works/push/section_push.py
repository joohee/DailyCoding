import boto3
from sns import SNSObject
import json
import os, sys
import send_push

if __name__ == "__main__":
    message = "test message"
    send_push.push('section', message)
