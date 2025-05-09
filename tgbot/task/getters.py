from datetime import datetime

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


async def on_title_entered(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    dialog_manager.dialog_data["title"] = message.text
    await dialog_manager.next()


async def on_description_entered(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    dialog_manager.dialog_data["description"] = message.text
    await dialog_manager.next()


async def on_due_date_entered(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    try:
        due_date = datetime.strptime(message.text, "%d.%m.%Y %H:%M")
        dialog_manager.dialog_data["due_date"] = due_date.isoformat()
        dialog_manager.dialog_data["due_date_display"] = message.text

        await dialog_manager.next()

    except ValueError:
        await message.answer(
            "❌ Неверный формат даты!\n"
            "Пожалуйста, введите дату в формате: <b>ДД.ММ.ГГГГ ЧЧ:ММ</b>\n"
            "Пример: 31.12.2024 23:59",
            parse_mode="HTML"
        )


async def on_tags_entered(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    tags = [tag.strip() for tag in message.text.split(",")]
    dialog_manager.dialog_data["tags"] = tags
    await dialog_manager.next()


async def get_task_data(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.dialog_data
    return {
        "title": data.get("title", "не указано"),
        "description": data.get("description", "не указано"),
        "due_date": data.get("due_date_display", "не указано"),
        "tags": ", ".join(data.get("tags", [])) or "не указаны",
    }
