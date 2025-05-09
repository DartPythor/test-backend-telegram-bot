import aiohttp
import asyncio
import logging
from urllib.parse import urljoin


import tgbot.service.type_objects as type_objects

logger = logging.getLogger(__name__)


class ServiceAPI:
    base_url = "http://localhost:8000"

    def __init__(self):
        logger.debug("Инициализация ServiceAPI")
        self.session = aiohttp.ClientSession()
        logger.info(f"Создан клиент API")

    async def close(self):
        logger.debug("Закрытие сессии API")
        await self.session.close()
        logger.info("Сессия API успешно закрыта")

    async def _post(self, url, data) -> dict:
        logger.debug(f"POST запрос к {url} с данными: {data}")
        async with self.session.post(url, data=data) as response:
            response.raise_for_status()
            data = await response.json()
            logger.debug(f"Успешный POST ответ от {url}")
            return data

    async def _get(self, url, data) -> dict:
        logger.debug(f"GET запрос к {url} с параметрами: {data}")
        async with self.session.get(url, params=data) as response:
            response.raise_for_status()
            data = await response.json()
            logger.debug(f"Успешный GET ответ от {url}")
            return data

    async def _delete(self, url, data) -> dict:
        logger.debug(f"DELETE запрос к {url} с параметрами: {data}")
        async with self.session.delete(url, data=data) as response:
            response.raise_for_status()
            data = await response.json()
            logger.debug(f"Успешный GET ответ от {url}")
            return data

    async def create_user(
        self, user: type_objects.CustomUserCreate
    ) -> type_objects.CustomUserResponse:
        url = urljoin(self.base_url, "users/api/v1/users/")
        data = user.model_dump()
        response = await self._post(url, data)
        return type_objects.CustomUserResponse(**response)

    async def create_task(self, task: type_objects.TaskCreate, telegram_id: int) -> type_objects.TaskResponse:
        url = urljoin(self.base_url, f"tasks/api/v1/task/?telegram_id={telegram_id}")
        data = task.model_dump()
        response = await self._post(url, data)
        return type_objects.TaskResponse(**response)

    async def get_info_task(self, task_id: str) -> dict:
        ...

    async def delete_task(self, task_id: str) -> dict:
        ...

    async def create_category(self, telegram_id: int) -> dict:
        ...

    async def delete_category(self, category_id: str) -> dict:
        ...


async def main():
    service = ServiceAPI()
    user = type_objects.CustomUserCreate(telegram_id=10025, username="massxs121", password="q2112122")
    print(await service.create_user(user))

if __name__ == "__main__":
    asyncio.run(main())
