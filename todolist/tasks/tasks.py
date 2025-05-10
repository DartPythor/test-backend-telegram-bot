# celery -A todolist worker -l info -P gevent
import json
from urllib.parse import urljoin

from celery import shared_task
from django.utils import timezone
import requests

from tasks.models import Tasks
from todolist.settings import TGBOT_HOST


@shared_task
def send_notification():
    tasks = Tasks.objects.filter(
        is_send_deadline=False,
        due_date__gt=timezone.now(),
    )
    data_send = [
        {"title": task.title, "telegram_id": task.user.telegram_id} for task in tasks
    ]
    data_send = json.dumps(data_send)
    response = requests.post(
        urljoin(TGBOT_HOST, "api/data"),
        data=data_send,
    )
