from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заметки")],
        [KeyboardButton(text="Категории")],
    ],
    resize_keyboard=True,
)
