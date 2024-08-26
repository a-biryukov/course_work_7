from datetime import timedelta, datetime

import requests
import pytz

from config.settings import TELEGRAM_TOKEN, TIME_ZONE
from habits.models import Habit


def send_telegram_message(habits: list) -> None:
    """
    Отправляет уведомления в телеграм
    :param habits: Список объектов класса Habit
    """
    for habit in habits:
        text = f'У Вас запланировано {habit.action} в {habit.place}'
        chat_id = habit.user.chat_id

        params = {
            'text': text,
            'chat_id': chat_id
        }

        requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', params=params)


def get_habits() -> list:
    """
    Получает объекты класса Habit, которым нужно отправить уведомления
    :return: Список объектов класса Habit
    """
    days_of_week = {
        7: 'monday',
        1: 'tuesday',
        2: 'wednesday',
        3: 'thursday',
        4: 'friday',
        5: 'saturday',
        6: 'sunday'
    }
    zone = pytz.timezone(TIME_ZONE)
    datetime_now = datetime.now(zone)
    day_of_week_today = datetime_now.weekday()
    time_send_message_1 = (datetime_now + timedelta(minutes=5)).time()
    time_send_message_2 = (datetime_now + timedelta(minutes=8)).time()

    params = {
        'user__chat_id__isnull': False,
        f'daysofweek__{days_of_week[day_of_week_today]}': True
    }

    habits = Habit.objects.filter(**params)

    habits = (
        habits.filter(runtime__time_1__gte=time_send_message_1, runtime__time_1__lte=time_send_message_2) |
        habits.filter(runtime__time_2__gte=time_send_message_1, runtime__time_2__lte=time_send_message_2) |
        habits.filter(runtime__time_3__gte=time_send_message_1, runtime__time_3__lte=time_send_message_2) |
        habits.filter(runtime__time_4__gte=time_send_message_1, runtime__time_4__lte=time_send_message_2) |
        habits.filter(runtime__time_5__gte=time_send_message_1, runtime__time_5__lte=time_send_message_2)
    )

    return habits
