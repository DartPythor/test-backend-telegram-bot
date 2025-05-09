from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from tasks.serializers import CategorySerializer, TaskSerializer
from tasks.models import Categories, Tasks
from users.models import CustomUser


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    lookup_field = "task_id"
    pagination_class = PageNumberPagination
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.data["user"])


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "task_id"


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "category_id"
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Categories.objects.filter(user=self.request.data["user"])


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "category_id"
