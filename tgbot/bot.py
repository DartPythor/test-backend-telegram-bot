import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from aiohttp import web

from config import TOKEN_BOT
from handlers.start import router as cmd_router
from task.handlers import router as task_router
from category.handlers import router as category_router
from task.dialog import get_dialog_task, get_tasks_dialog, get_delete_tasks_dialog
from category.dialog import (
    get_dialog_category,
    get_categories_dialog,
    get_delete_categories_dialog,
)
from notification.aiohttp_server import handle_request


async def start_aiohttp(app):
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 9000)
    await site.start()
    print(f"AioHTTP server started on port {9000}")


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_BOT)
    dp = Dispatcher(storage=MemoryStorage())

    aiohttp_app = web.Application()
    aiohttp_app["bot"] = bot
    aiohttp_app.router.add_post('/api/data', handle_request)

    setup_dialogs(dp)
    dp.include_router(cmd_router)
    dp.include_router(task_router)
    dp.include_router(category_router)
    dp.include_router(get_dialog_task())
    dp.include_router(get_dialog_category())
    dp.include_router(get_categories_dialog())
    dp.include_router(get_delete_categories_dialog())
    dp.include_router(get_tasks_dialog())
    dp.include_router(get_delete_tasks_dialog())

    await asyncio.gather(
        dp.start_polling(bot),
        start_aiohttp(aiohttp_app)
    )


if __name__ == "__main__":
    asyncio.run(main())
