#from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied

# Create your views here.
from userapi.serializers import UserSerializer
from django.contrib.auth.models import User
from userapi.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    List all Users
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,) # prevents a user to see the post form if they are not authenticated
    queryset = User.objects.all() # list all the books


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    serializer_class = UserSerializer
    queryset = User.objects.all()

