from rest_framework import generics
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
