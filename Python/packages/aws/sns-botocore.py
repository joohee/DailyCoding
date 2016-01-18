import botocore.session

# establish a session and set credentials
sesh = botocore.session.get_session()
access_key = "AKIAJUNFGU4AUS4AXADQ"
secret_key = "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"

sesh.set_credentials(access_key=access_key, secret_key=secret_key)

#get SNS service and set endpoint
sns = sesh.get_service('sns')
endpoint = sns.get_endpoint('ap-northeast-1') #or another AWS region

#set up a Publish call and execute it
op = sns.get_operation('Publish')
topic_arn = "arn:aws:sns:ap-northeast-1:563795231896:TOPIC_ARN"
http_response, response_data = op.call(topic_arn=topic_arn, subject='test', message='hello', endpoint=endpoint)

print(http_response)
print(response_data)
