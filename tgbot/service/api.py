import aiohttp
import asyncio
import logging
from urllib.parse import urljoin


import service.type_objects as type_objects

logger = logging.getLogger(__name__)


class ServiceAPI:
    base_url = "http://localhost:8000"

    def __init__(self):
        logger.debug("Инициализация ServiceAPI")
        logger.info(f"Создан клиент API")

    async def close(self):
        logger.debug("Закрытие сессии API")
        await self.session.close()
        logger.info("Сессия API успешно закрыта")

    async def _post(self, url, data) -> dict:
        logger.debug(f"POST запрос к {url} с данными: {data}")
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                response.raise_for_status()
                data = await response.json()
                logger.debug(f"Успешный POST ответ от {url}")
                print(data)
                return data

    async def _get(self, url, data) -> dict:
        logger.debug(f"GET запрос к {url} с параметрами: {data}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=data) as response:
                response.raise_for_status()
                data = await response.json()
                logger.debug(f"Успешный GET ответ от {url}")
                return data

    async def _delete(self, url, data) -> dict:
        logger.debug(f"DELETE запрос к {url} с параметрами: {data}")
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, params=data) as response:
                response.raise_for_status()
                logger.debug(f"Успешный DELETE ответ от {url}")
                return data

    async def create_user(
        self, user: type_objects.CustomUserCreate
    ) -> type_objects.CustomUserResponse:
        url = urljoin(self.base_url, "users/api/v1/users/")
        data = user.model_dump()
        response = await self._post(url, data)
        return type_objects.CustomUserResponse(**response)

    async def create_task(
        self, task: type_objects.TaskCreate
    ) -> type_objects.TaskResponse:
        url = urljoin(self.base_url, f"tasks/api/v1/task/")
        data = task.model_dump()
        response = await self._post(url, data)
        return type_objects.TaskResponse(**response)

    async def get_tasks(self, telegram_id: int, page: int = 1) -> dict:
        url = urljoin(self.base_url, f"tasks/api/v1/task/")
        params = {
            "user": telegram_id,
            "page": page,
        }
        response = await self._get(url, params)
        return response

    async def delete_task(self, task_id: str) -> dict:
        url = urljoin(self.base_url, f"tasks/api/v1/task/{task_id}/")
        params = None
        response = await self._delete(url, params)
        return response

    async def detail_task(self, task_id: str) -> type_objects.TaskDetailResponse:
        url = urljoin(self.base_url, f"tasks/api/v1/task/{task_id}/")
        params = None
        response = await self._get(url, params)
        return type_objects.TaskDetailResponse(**response)

    async def detail_category(self, category_id: str) -> type_objects.CategoryDetail:
        url = urljoin(self.base_url, f"tasks/api/v1/category/{category_id}/")
        params = None
        response = await self._get(url, params)
        return type_objects.CategoryDetail(**response)

    async def create_category(
        self, category: type_objects.CategoryCreate
    ) -> type_objects.CategoryResponse:
        url = urljoin(self.base_url, f"tasks/api/v1/category/")
        data = category.model_dump()
        response = await self._post(url, data)
        return type_objects.CategoryResponse(**response)

    async def get_categories(self, telegram_id: int, page: int = 1) -> dict:
        url = urljoin(self.base_url, f"tasks/api/v1/category/")
        params = {
            "user": telegram_id,
            "page": page,
        }
        response = await self._get(url, params)
        return response

    async def delete_category(self, category_id: str) -> dict:
        url = urljoin(self.base_url, f"tasks/api/v1/category/{category_id}/")
        params = None
        response = await self._delete(url, params)
        return response


async def main():
    service = ServiceAPI()
    # user = type_objects.CustomUserCreate(
    #     telegram_id=10025, username="massxs121", password="q2112122"
    # )
    category = type_objects.CategoryCreate(
        user=1111,
        name="123",
    )
    print(await service.create_category(category))


if __name__ == "__main__":
    asyncio.run(main())
