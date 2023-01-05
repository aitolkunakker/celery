from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Алтивируйте фллфутн перейдя по ссылке\n{activation_link}'
    send_mail('Activation account', message, 'aitolkuns52@gmail.com', [email])
    return 'отправлено'
