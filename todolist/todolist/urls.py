from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls", namespace="tasks")),
    path("users/", include("users.urls", namespace="users")),
]
