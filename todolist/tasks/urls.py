from django.urls import path

from tasks.views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
)

app_name = "task"

urlpatterns = [
    path(
        "api/v1/task/",
        TaskListCreateAPIView.as_view(),
        name="task-create",
    ),
    path(
        "api/v1/task/<str:task_id>/",
        TaskRetrieveUpdateDestroyAPIView.as_view(),
        name="task-get-update-delete",
    ),
    path(
        "api/v1/category/",
        CategoryListCreateAPIView.as_view(),
        name="category-create",
    ),
    path(
        "api/v1/category/<str:category_id>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-get-update-delete",
    ),
]
