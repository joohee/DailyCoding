import boto3
import json
import datetime

""" Amazon SQS 를 이용한 예제를 나타냅니다. 

   도움말을 보려면 아래 명령어를 입력하세요.
        pydoc sqs


"""
class SQSObject:
    """ boto3 을 통해 SQS를 이용한 기능이 포함된 Class입니다. 
        
        도움말을 html 파일로 생성하려면 아래 명령어를 입력하세요. 
            pydoc -w sqs
    

        Init: 
            profile_name이 필요합니다. 일반적으로 ~/.aws/credentials에 추가하여 사용합니다.
            region까지 지정하고 싶을 경우에 ~/.aws/config 에 기록하고, credentials 에 기록한 profile을 사용합니다.

        Methods:
            - get_queue(queue_name)
            : Queue를 반환합니다. 없으면 SystemExit Error를 발생시킵니다.
            - send_message(queue_name, message_body) 
            : 특정 Queue에 메세지를 전송합니다.
            - get_message(queue_name, max_number_of_message, delete_before_return)
            : 특정 Queue에서 지정한 크기만큼 메세지를 가져옵니다. 갯수는 1-10개까지 요청할 수 있으며    
            실제 가져오는 메세지는 요청 숫자보다 적을 수 있습니다.
            Queue로부터 가져올 때 메세지를 삭제할 것인지 옵션으로 처리할 수 있습니다. // TODO  기능확인 필요.

            http://boto3.readthedocs.org/en/latest/reference/services/sqs.html#SQS.Client.delete_message

        Exceptions: 
            botocore.exceptions.ClientError: An error occurred (InvalidClientTokenId) when calling the ListQueues operation: The security token included in the request is invalid.
            위와 같은 에러 메세지가 발생할 경우, ~/.aws/credentials 에 등록된 accessKey/secretKey가 유효하지 않기 때문입니다. 
            따라서 적절한 키가 설정 되었는지 확인해야 합니다. 
   """ 
    
    def __init__(self, profile_name):
        self.session = boto3.Session(profile_name=profile_name)
        self.client = self.session.client('sqs')
        self.sqs = self.session.resource('sqs')
        for queue in self.sqs.queues.all():
            print(queue.url)
        pass

    def get_queue(self, queue_name):
        queue = self.sqs.get_queue_by_name(QueueName=queue_name)
        if queue != None:
            return queue
        else:
            print("Check QueueName: {}".format(queue_name))
            raise SystemExit
        
    def send_message(self, queue_name, message_body):
        queue = self.get_queue(queue_name)
        response = queue.send_message(MessageBody=message_body)
        print("Success to send a message...")
        print(response)

    def get_message(self, queue_name, max_number_of_messages=1, delete_before_return=True):
        queue = self.get_queue(queue_name)
        messages = queue.receive_messages(MaxNumberOfMessages=max_number_of_messages)
        for message in messages: 
            if delete_before_return == True:
                message.delete()
                print("message deleted...{}".format(message.body))
        return messages


if __name__ == '__main__':
    sqs = SQSObject('dev_internal')
    message = {}
    message['key'] = 'test'
    message['date'] = datetime.datetime.now().strftime('%Y%m%d-%H%M%s')

    sqs.send_message('test-for-joey', json.dumps(message))
    messages = sqs.get_message('test-for-joey', 10,  True)

    print("count: {}".format(str(len(messages))))
    for message in messages: 
        print("message: {}".format(message))
        print("body: {}".format(message.body))
