import requests

from config.settings import TG_API
from atomichabits.models import Habit
from atomichabits.services import send_message_tg

from celery import shared_task


@shared_task
def check_user_habits_and_send():
    """ Отправка пользователю привычки """

    print('Запуск программы')

    habits = Habit.objects.all()

    for habit in habits:
        message = f'Внимание!' \
                  f'\n{habit}'
        params = {
            'chat_id': habit.owner.telegram_chat_id,
            'text': message
        }

        create_url_message_to_user = f'https://api.telegram.org/bot' \
                                     f'{TG_API}/sendMessage?'

        print(
            f'Выполняется отправка сообщения:'
            f'\nКому:{habit.owner.telegram_username}'
            f'\nСообщение: {message}'
            f'\nПоследнее напоминание: {habit.last_send}'
            f'\nвремя привычки {habit.time} время сейчас - '
        )

        send_message_tg(habit, create_url_message_to_user, params)

# def check_user_habits_and_send():
#     """Направляем пользователю уведомление в Telegram"""
#
#     habits = Habit.objects.all()
#     for habit in habits:
#         message = f'\nВнимание!' \
#                   f'\n{habit}'
#         chat_id = habit.owner.telegram_chat_id
#         url = f"https://api.telegram.org/bot{TG_API}/sendMessage?chat_id={chat_id}&text={message}"
#         requests.get(url).json()




