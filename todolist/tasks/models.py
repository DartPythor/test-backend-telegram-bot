import hashlib

from django.conf import settings
from django.db import models
from django.utils import timezone


class Categories(models.Model):
    category_id = models.CharField(
        primary_key=True,
        max_length=64,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories",
    )
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.category_id:
            raw_id = f"{self.name}_{self.user.telegram_id}_{timezone.now().timestamp()}"
            self.category_id = hashlib.sha256(raw_id.encode()).hexdigest()[:24]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.telegram_id} - {self.name}"


class Tasks(models.Model):
    task_id = models.CharField(
        primary_key=True,
        max_length=64,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        to_field="telegram_id",
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Categories")
    created_at = models.DateTimeField(auto_now_add=True)
    is_send_deadline = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.task_id:
            raw_id = (
                f"{self.title}_{self.user.telegram_id}_{timezone.now().timestamp()}"
            )
            self.task_id = hashlib.sha256(raw_id.encode()).hexdigest()[:24]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.telegram_id} - {self.title}"
