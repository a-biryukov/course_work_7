from celery import shared_task

from telegram.services import get_habits, send_telegram_message


@shared_task
def sending_notification():
    habits = get_habits()
    send_telegram_message(habits)
