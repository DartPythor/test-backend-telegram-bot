from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboard.reply_menu import main_menu
from tgbot.lexicon.commands_texts import CommandTexts
from tgbot.service.api import ServiceAPI
from tgbot.service.type_objects import CustomUserCreate

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    service = ServiceAPI()
    await message.answer(
        text=CommandTexts.get_start_text(),
        parse_mode=ParseMode.HTML,
        reply_markup=main_menu,
    )

    await service.create_user(
        CustomUserCreate(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            password="example1",
        )
    )
