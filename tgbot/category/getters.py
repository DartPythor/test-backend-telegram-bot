from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


async def on_name_entered(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    dialog_manager.dialog_data["name"] = message.text
    await dialog_manager.next()


async def get_category_data(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.dialog_data
    return {
        "name": data.get("name", "не указано"),
    }
