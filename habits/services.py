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

    requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
