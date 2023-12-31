# import requests
#
# from django.core.management import BaseCommand
#
# from atomichabits.models import Habit
# from config.settings import TG_API_KEY, TG_URL
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **kwargs):
#
#         chai_id = requests.get(f'https://api.telegram.org/bot{TG_API_KEY}/getUpdates')
#         print(f"\nИнформация о ТГ боте:\n{chai_id.json()}")
#         print(f"\nВаш чат id: {chai_id.json()['result'][0]['message']['from']['id']}\n")
#
#         habits = Habit.objects.all()
#         for habit in habits:
#             message = f'\nВнимание!' \
#                       f'\n{habit}'
#             params = {
#                 'chat_id': habit.owner.telegram_chat_id,
#                 'text': message
#             }
#             create_url_message_to_user = f'{TG_URL}{TG_API_KEY}/sendMessage?chat_id={habit.owner.telegram_chat_id}&text={message}'
#
#             print(create_url_message_to_user)
#             requests.get(f'{TG_URL}{TG_API_KEY}/sendMessage?', params=params)
