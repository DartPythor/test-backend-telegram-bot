from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

task_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мои задачи", callback_data="task-list")],
        [InlineKeyboardButton(text="Создать задачу", callback_data="task-create")],
        [InlineKeyboardButton(text="Удалить задачу", callback_data="task-delete")],
    ],
    resize_keyboard=True,
)
