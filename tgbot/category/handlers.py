from aiogram import F, Router

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.category.state import CategoryState
from tgbot.keyboard.task_menu import category_menu

router = Router()

@router.callback_query(F.data == "category-create")
async def start_task_create(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(CategoryState.name, mode=StartMode.RESET_STACK)


@router.message(F.text == "Теги")
async def show_task_menu(message: Message, dialog_manager: DialogManager):
    await message.answer(
        "Меню задач:",
        reply_markup=category_menu,
    )
