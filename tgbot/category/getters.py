from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput

from tgbot.service.api import ServiceAPI


async def on_name_entered(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
):
    dialog_manager.dialog_data["name"] = message.text
    await dialog_manager.next()


async def get_category_data(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.dialog_data
    return {
        "name": data.get("name", "не указано"),
    }


async def on_id_entered(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
):
    dialog_manager.dialog_data["category_id"] = message.text
    await dialog_manager.next()


async def get_category_data_delete(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.dialog_data
    return {
        "category_id": data.get("category_id", "не указано"),
    }


async def category_getter(dialog_manager: DialogManager, **kwargs):
    api_client = ServiceAPI()
    page = dialog_manager.dialog_data.get("page", 1)
    user_id = dialog_manager.event.from_user.id
    response = await api_client.get_categories(telegram_id=user_id, page=page)

    return {
        "categories": response["results"],
        "current_page": page,
        "total_pages": (response["count"] // 5) + 1,
        "has_next": bool(response["next"]),
        "has_previous": bool(response["previous"]),
    }


async def on_prev_page(callback: CallbackQuery, button: Button, manager: DialogManager):
    current_page = manager.dialog_data.get("page", 1)
    manager.dialog_data["page"] = max(1, current_page - 1)
    await manager.show()

async def on_next_page(callback: CallbackQuery, button: Button, manager: DialogManager):
    current_page = manager.dialog_data.get("page", 1)
    total_pages = (manager.dialog_data.get("total_items", 0) // 5) + 1
    manager.dialog_data["page"] = min(total_pages, current_page + 1)
    await manager.show()
