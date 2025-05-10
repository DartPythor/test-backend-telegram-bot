from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from service.api import ServiceAPI
from service import type_objects


async def on_confirm(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    service = ServiceAPI()
    category = type_objects.CategoryCreate(
        user=callback.from_user.id,
        name=dialog_manager.dialog_data["name"],
    )
    await service.create_category(category)
    await dialog_manager.done()
    await callback.message.answer("Тег создан!")


async def on_confirm_delete(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    service = ServiceAPI()
    category_id = dialog_manager.dialog_data["category_id"]
    await service.delete_category(category_id)
    await dialog_manager.done()
    await callback.message.answer("Тег удален!")
