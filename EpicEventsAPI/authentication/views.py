from django.shortcuts import render

# Create your views here.
from authentication.models import User
from rest_framework import permissions, viewsets

from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
