from django.urls import path
from users.views import CustomUserCreateAPIView

app_name = "users"

urlpatterns = [
    path("api/v1/users/", CustomUserCreateAPIView.as_view(), name="user-create"),
]
