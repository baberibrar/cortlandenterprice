from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
