from aiohttp import web
import json


from aiogram import Bot


async def handle_request(request: web.Request):
    data_get = await request.json()
    print("Получены данные:", data_get)

    bot: Bot = request.app["bot"]

    for data in data_get:
        try:
            await bot.send_message(
                chat_id=data["telegram_id"],
                text=f"{data['title']} - дедлайн вышел!"
            )
            response_data = {"status": "success"}
        except Exception as e:
            response_data = {"status": "error", "details": str(e)}

    return web.Response(
        text=json.dumps(response_data),
        content_type="application/json"
    )
