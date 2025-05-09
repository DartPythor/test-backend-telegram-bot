import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from tgbot.config import TOKEN_BOT
from tgbot.handlers.start import router as cmd_router
from tgbot.task.handlers import router as task_router
from tgbot.category.handlers import router as category_router
from tgbot.task.dialog import get_dialog_task
from tgbot.category.dialog import get_dialog_category



async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_BOT)
    dp = Dispatcher(storage=MemoryStorage())

    setup_dialogs(dp)
    dp.include_router(cmd_router)
    dp.include_router(task_router)
    dp.include_router(category_router)
    dp.include_router(get_dialog_task())
    dp.include_router(get_dialog_category())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
