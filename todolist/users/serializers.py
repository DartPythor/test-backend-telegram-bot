from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "telegram_id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "telegram_id": {"required": True}
        }

    def validate_telegram_id(self, value):
        if CustomUser.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("Пользователь с таким Telegram ID уже существует")
        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
