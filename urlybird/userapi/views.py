#from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from userapi.serializers import UserSerializer
from django.contrib.auth.models import User
from userapi.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    List all Users
    """
    
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,) # prevents a user to see the post form if they are not authenticated
    queryset = User.objects.all() # list all the books


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAdminUser)
    serializer_class = UserSerializer
    queryset = User.objects.all()

