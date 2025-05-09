from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Задачи")],
        [KeyboardButton(text="Теги")],
    ],
    resize_keyboard=True,
)
