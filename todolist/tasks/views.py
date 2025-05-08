from rest_framework import generics
from rest_framework.exceptions import ValidationError

from tasks.serializers import CategorySerializer, TaskSerializer
from tasks.models import Categories, Tasks
from users.models import CustomUser


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    lookup_field = "task_id"

    def get_queryset(self):
        telegram_id = self.request.query_params.get("telegram_id", None)
        if telegram_id is None:
            raise ValidationError({"telegram_id": "This field is required."})
        try:
            user = CustomUser.objects.get(telegram_id=telegram_id)
        except CustomUser.DoesNotExist:
            raise ValidationError({"telegram_id": "Invalid telegram_id."})

        return Tasks.objects.filter(user=user)

    def perform_create(self, serializer):
        user = CustomUser.objects.get(telegram_id=self.request.data["telegram_id"])
        serializer.save(user=user)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    lookup_field = "task_id"


class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get("telegram_id", None)
        if telegram_id is None:
            raise ValidationError({"telegram_id": "This field is required."})
        try:
            user = CustomUser.objects.get(telegram_id=telegram_id)
        except CustomUser.DoesNotExist:
            raise ValidationError({"telegram_id": "Invalid telegram_id."})

        return Categories.objects.filter(user=user)

    def perform_create(self, serializer):
        user = CustomUser.objects.get(telegram_id=self.request.data["telegram_id"])
        serializer.save(user=user)


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    lookup_field = "category_id"
