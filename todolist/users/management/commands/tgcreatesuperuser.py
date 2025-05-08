from getpass import getpass

from django.core.management import CommandError
from django.contrib.auth.management.commands.createsuperuser import (
    Command as BaseCommand,
)
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser


class Command(BaseCommand):
    help = _("Создание суперпользователя с Telegram ID")

    def handle(self, **options):
        telegram_id = input(_("Введите Telegram ID: "))

        if CustomUser.objects.filter(telegram_id=telegram_id).exists():
            raise CommandError(_("Пользователь с таким Telegram ID уже существует"))

        username = input(_("Введите username: "))

        if CustomUser.objects.filter(username=username).exists():
            raise CommandError(_("Пользователь с таким username уже существует"))

        password = getpass(prompt=_("Введите пароль: "), stream=None)

        try:
            user = CustomUser.objects.create_superuser(
                username=username,
                telegram_id=telegram_id,
                password=password,
            )
            self.stdout.write(
                _("Суперпользователь {0} создан!").format(user.telegram_id)
            )
        except Exception as e:
            raise CommandError(_("Ошибка: {0}").format(str(e)))
