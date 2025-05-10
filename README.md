# ToDo List Telegram Bot с Django Backend

Телеграм-бот для управления задачами, интегрированный с Django REST API. Проект включает бекенд на Django, асинхронного бота на Aiogram, Celery для уведомлений и Docker для развертывания.

## 📋 Требования

- Docker
- Docker Compose
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))

## 🚀 Быстрый старт

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/yourusername/todo-bot-project.git
   cd todo-bot-project
   ```
2. **Создайте файл .env**
   ```bash
   copy tgbot/example.env .env
   ```
   Поместите туда токен своего бота.
3. **Сборка и запуск докера**
   ```bash
   docker-compose build
   docker-compose up
   ```
## 🏗 Архитектура
**Компоненты:**

*   **Django (DRF):**
    *   Модели: `Todo`, `Category`, кастомный `User`.
    *   API: CRUD для задач и категорий.
    *   Админка: управление сущностями.
    *   Часовой пояс: `America/Adak`.

*   **Telegram Bot (Aiogram):**
    *   Диалоги с пользователем через `aiogram-dialog`.
    *   Асинхронные HTTP-запросы к API через `aiohttp`.
    *   Валидация данных с `pydantic`.

*   **Celery:**
    *   Периодическая проверка просроченных задач.
    *   Отправка уведомлений через бота.

*   **Инфраструктура:**
    *   PostgreSQL: хранение данных.
    *   Redis: брокер для Celery и кэширование.
    *   Docker: изоляция сервисов.

## 🛑 Трудности и решения
1. Никогда не работал с aiogram-dialog, но получилось не плохо, но нужна практика.
2. Необходимо переделать систему аккаунтов, сейчас она не доделана.
