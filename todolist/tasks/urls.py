from django.urls import path

from tasks.views import TaskListCreateAPIView

app_name = "task"

urlpatterns = [
    path(
        "api/v1/task/",
        TaskListCreateAPIView.as_view(),
        name="task-list-destroy-create",
    ),

]
