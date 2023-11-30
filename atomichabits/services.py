import datetime

import requests
from django.utils import timezone


def send_message_tg(habit, url, params):
    """ Отправки сообщения пользователю """

    now = timezone.now()

    if habit.last_send:
        if habit.last_send <= now:
            requests.get(url, params=params)
            habit.last_send = timezone.now()
            habit.save()

    else:
        if habit.time <= now:
            requests.get(url, params=params)
            habit.last_send = timezone.now()
            habit.save()
