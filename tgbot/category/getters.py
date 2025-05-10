from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput

from service.api import ServiceAPI
from category.state import CategoryListState

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

async def on_category_selected(
    callback: CallbackQuery,
    widget,
    manager: DialogManager,
    item_id: str,
):
    manager.dialog_data["category_id"] = item_id
    await manager.switch_to(CategoryListState.detail)


async def detail_getter(dialog_manager: DialogManager, **kwargs):
    category_id = dialog_manager.dialog_data["category_id"]
    service = ServiceAPI()
    category = await service.detail_category(category_id)
    return {
        "title": category.name,
        "id": category.category_id,
    }
