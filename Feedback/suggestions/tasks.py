from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_email_task_message(name, email, suggestion):
    print(f"Name: {name}, Type: {type(name)}")
    print(f"Email: {email}, Type: {type(email)}")
    print(f"Suggestion: {suggestion}, Type: {type(suggestion)}")
    sleep(10)
    send_mail(
        "Your suggestion has been received",
        f"Thank you for your suggestion: {suggestion}",
        "gabrielokemwa83@gmail.com",
        [email],
        fail_silently=False,
    )
