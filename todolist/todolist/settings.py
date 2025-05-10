from pathlib import Path

import environ
from dotenv import load_dotenv

env = environ.Env()
environ.Env.read_env()
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-404w206hqmsrr$%ohrat&8+)+pa(1%glg*ya8q3i33e4-e^l0j"

DEBUG = env("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    "tasks.apps.TasksConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "todolist.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "todolist.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_NAME", default="mydb"),
        "USER": env("POSTGRES_USER", default="myuser"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="mypassword"),
        "HOST": env("POSTGRES_HOST", cast=str, default="postgres"),
        "PORT": env("POSTGRES_PORT", cast=str, default="5432"),
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1000,  # Количество элементов на странице по умолчанию
}

LANGUAGE_CODE = "ru"

TIME_ZONE = "America/Adak"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

CELERY_BROKER_URL = (
    f"redis://{env('REDIS_HOST', cast=str, default='redis')}:6379/0"
)
CELERY_RESULT_BACKEND = (
    f"redis://{env('REDIS_HOST', cast=str, default='redis')}:6379/0"
)

CELERY_BEAT_SCHEDULE = {
    "send_notification": {
        "task": "tasks.tasks.send_notification",
        "schedule": 10,
    },
}

TGBOT_HOST = env("TGBOT_HOST", default="")
