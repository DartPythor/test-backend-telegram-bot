from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from tasks.models import Categories, Tasks
import datetime


class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            telegram_id=123456789,
            password="testpass123",
        )

        self.category = Categories.objects.create(user=self.user, name="Работа")

        self.task = Tasks.objects.create(
            user=self.user,
            title="Тестовая задача",
            due_date=datetime.datetime.now() + datetime.timedelta(days=1),
        )
        self.task.tags.add(self.category)

        self.task_list_url = reverse("task:task-create")
        self.task_detail_url = reverse(
            "task:task-get-update-delete", args=[self.task.task_id]
        )
        self.category_list_url = reverse("task:category-create")
        self.category_detail_url = reverse(
            "task:category-get-update-delete", args=[self.category.category_id]
        )

    def test_create_task(self):
        """Тест создания задачи"""
        data = {
            "title": "Новая задача",
            "due_date": datetime.datetime.now().isoformat(),
            "tags": [self.category.category_id],
            "telegram_id": 123456789,
        }
        response = self.client.post(self.task_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 2)

    def test_get_task_list(self):
        """Тест получения списка задач"""
        response = self.client.get(self.task_list_url, {"telegram_id": 123456789})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Тестовая задача")

    def test_task_detail(self):
        """Тест получения деталей задачи"""
        response = self.client.get(self.task_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Тестовая задача")

    def test_task_update(self):
        """Тест обновления задачи"""
        data = {"title": "Обновленная задача"}
        response = self.client.patch(self.task_detail_url, data)
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.task.title, "Обновленная задача")

    def test_task_delete(self):
        """Тест удаления задачи"""
        response = self.client.delete(self.task_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tasks.objects.count(), 0)

    def test_create_category(self):
        """Тест создания категории"""
        data = {"name": "Личное", "telegram_id": 123456789}
        response = self.client.post(self.category_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categories.objects.count(), 2)

    def test_get_category_list(self):
        """Тест получения списка категорий"""
        response = self.client.get(self.category_list_url, {"telegram_id": 123456789})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Работа")

    def test_category_detail(self):
        """Тест получения деталей категории"""
        response = self.client.get(self.category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Работа")

    def test_category_update(self):
        """Тест обновления категории"""
        data = {"name": "Обновленная категория"}
        response = self.client.patch(self.category_detail_url, data)
        self.category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.category.name, "Обновленная категория")

    def test_category_delete(self):
        """Тест удаления категории"""
        response = self.client.delete(self.category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Categories.objects.count(), 0)

    def test_missing_telegram_id(self):
        """Тест отсутствия обязательного параметра"""
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)

        response = self.client.get(self.category_list_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)

    def test_invalid_telegram_id(self):
        """Тест невалидного telegram_id"""
        response = self.client.get(self.task_list_url, {"telegram_id": 999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)

        response = self.client.get(self.category_list_url, {"telegram_id": 999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)
