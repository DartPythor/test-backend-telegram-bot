from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from service.api import ServiceAPI
from service import type_objects


async def on_confirm(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    service = ServiceAPI()
    task = type_objects.TaskCreate(
        title=dialog_manager.dialog_data["title"],
        description=dialog_manager.dialog_data["description"],
        due_date=dialog_manager.dialog_data["due_date"],
        tags=dialog_manager.dialog_data["tags"],
        user=callback.from_user.id,
    )
    await service.create_task(task)
    await dialog_manager.done()
    await callback.message.answer("Задача создана!")


async def on_confirm_delete(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    service = ServiceAPI()
    task_id = dialog_manager.dialog_data["task_id"]
    await service.delete_task(task_id)
    await dialog_manager.done()
    await callback.message.answer("Задача удалена!")
