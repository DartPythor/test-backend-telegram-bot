from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    telegram_id = models.PositiveBigIntegerField(
        verbose_name=_("телеграм id"),
        help_text=_("Телеграм id пользователя"),
        primary_key=True,
        unique=True,
    )
    USERNAME_FIELD = "telegram_id"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} - {self.telegram_id}"
