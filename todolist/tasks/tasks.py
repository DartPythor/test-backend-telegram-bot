# celery -A todolist worker -l info -P gevent
from celery import shared_task
from django.utils import timezone

from tasks.models import Tasks


@shared_task
def send_notification():
    tasks = Tasks.objects.filter(
        is_send_deadline=False,
        # due_date__gt=timezone.now(),
    )

    data_send = [{task.task_id: task.user.telegram_id} for task in tasks]

    print(data_send)
    return True
