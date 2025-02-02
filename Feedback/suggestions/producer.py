import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials = pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()
channel.queue_declare(queue='mail_queue', durable=True)


def send_email_task_message(task_message):
    channel.basic_publish(
        exchange='',
        routing_key='mail_queue',
        body=json.dumps(task_message),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    print(" [x] Sent %r" % task_message)
    connection.close()


