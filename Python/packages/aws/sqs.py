import boto3
import json
import datetime

class SQSObject:
    
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

    def get_message(self, queue_name, max_number_of_messages=1):
        queue = self.get_queue(queue_name)
        for message in queue.receive_messages(MaxNumberOfMessages=max_number_of_messages):
            print("message: {}".format(message))
            print("body: {}".format(message.body))
            message.delete()


if __name__ == '__main__':
    sqs = SQSObject('dev_internal')
    message = {}
    message['key'] = 'test'
    message['date'] = datetime.datetime.now().strftime('%Y%m%d-%H%M%s')

    sqs.send_message('test-for-joey', json.dumps(message))
    sqs.get_message('test-for-joey')
