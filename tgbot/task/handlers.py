from aiogram import F, Router

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode

from task.state import TaskState, TaskListState, TaskDeleteState
from keyboard.task_menu import task_menu

router = Router()

@router.callback_query(F.data == "task-create")
async def start_task_create(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(TaskState.title, mode=StartMode.RESET_STACK)


@router.callback_query(F.data == "task-list")
async def start_task_create(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(TaskListState.list, mode=StartMode.RESET_STACK)


@router.callback_query(F.data == "task-delete")
async def start_task_create(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(TaskDeleteState.task_id, mode=StartMode.RESET_STACK)


@router.message(F.text == "Задачи")
async def show_task_menu(message: Message, dialog_manager: DialogManager):
    await message.answer(
        "Меню задач:",
        reply_markup=task_menu,
    )
