from datetime import datetime, timedelta
import json

import requests
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from config import settings


def send_telegram_message(chat_id, message):
    print('Сообщение')
    params = {
        'text': message,
        'chat_id': chat_id
    }

    response = requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)


def create_periodic_task(username, habit_id, hour, minute, week_list, message, chat_id):
    """Создает периодическую задачу"""

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=50,
        period=IntervalSchedule.SECONDS,
    )
    # schedule = crontab()

    periodic_task, created = PeriodicTask.objects.get_or_create(
        name=f"habit_{habit_id}_{username}",
        task="send_information_about_habit",
        interval=schedule,
        args=([]),
        kwargs=json.dumps({
            "message": message,
            "tg_chat_id": chat_id
        }),
    )

    if created:
        periodic_task.expires = datetime.utcnow() + timedelta(seconds=30)
        periodic_task.save()
    print(f"task={periodic_task}, удалось создать")


def disable_periodic_task(username, habit_id):
    task = PeriodicTask.objects.get(name=f"habit_{habit_id}_{username}")
    task.enabled = False
    task.save()

    print(f"task={task}, удалось отключить")