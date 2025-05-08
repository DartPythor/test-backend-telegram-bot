from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from django.contrib.auth.hashers import check_password

class CustomUserTests(APITestCase):
    def setUp(self):
        self.url = reverse("users:user-create")
        self.existing_user = CustomUser.objects.create(
            telegram_id=123456789,
            username="existing_user",
            password="testpass123"
        )

    def test_create_user_success(self):
        """Тест успешного создания пользователя"""
        data = {
            "telegram_id": 987654321,
            "password": "newpass123",
            "username": "new_user"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(telegram_id=987654321).exists())

    def test_missing_required_fields(self):
        """Тест отсутствия обязательных полей"""
        response = self.client.post(self.url, {"password": "pass123"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('telegram_id', response.data)

        response = self.client.post(self.url, {"telegram_id": 123})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_duplicate_telegram_id(self):
        """Тест дублирования telegram_id"""
        data = {
            "telegram_id": 123456789,
            "password": "duplicatepass",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("telegram_id", response.data)

    def test_password_hashing(self):
        """Тест корректного хэширования пароля"""
        data = {
            "telegram_id": 555555555,
            "password": "securepassword",
            "username": "test1",
        }
        response = self.client.post(self.url, data)
        user = CustomUser.objects.get(telegram_id=555555555)
        self.assertTrue(check_password("securepassword", user.password))

    def test_partial_update_not_allowed(self):
        """Тест отсутствия нереализованных методов"""
        detail_url = reverse("users:user-create") + '123/'
        response = self.client.patch(detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_data_types(self):
        """Тест невалидных типов данных"""
        data = {
            "telegram_id": "invalid_string",
            "password": "pass123"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            "telegram_id": 888888888,
            "password": 12345678
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
