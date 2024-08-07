import json
import pika
from django.core.mail import send_mail
from time import sleep


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials = pika.PlainCredentials('guest', 'guest')))

channel = connection.channel()
channel.queue_declare(queue='mail_queue', durable=True)


def callback(ch , method , properties , body):
    task_message = json.loads(body)
    sleep(10)
    send_mail(
        'New suggestion from %s' % task_message['name'],
        task_message['suggestion'],
        "gabrielokemwa83@gmail.com",
        [task_message['email']],
        fail_silently=False,
    )
    ch.basic_ack(delivery_tag = method.delivery_tag)

def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='mail_queue', on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()