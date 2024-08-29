from celery import shared_task
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_information(email):
    message = "Необходимо совершить действие"
    send_mail('Действие', 'Необходимо совершить действие', EMAIL_HOST_USER, [email])
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        print(user.tg_chat_id)
        send_telegram_message(user.tg_chat_id, message)

@shared_task
def send_telegram_message(email):
    """
    Отправляем напоминание пользователю.
    :param email:
    :return:
    """
    today = timezone.now().today()
    print(today)
