#from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
from api.serializers import BookmarkListSerializer, BookmarkDetailSerializer, ClickDetailSerializer
from breveurl.models import Bookmark
from click.models import Click
from api.permissions import IsOwnerOrReadOnly
from breveurl import views as breve_views

class BookmarkViewSet(viewsets.ModelViewSet):
    
    queryset = Bookmark.objects.all() # list all the books
    serializer_class = BookmarkListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) # prevents a user to see the post form if they are not authenticated
    authentication_classes = (JSONWebTokenAuthentication, )
    def perform_create(self, serializer):
        serializer.save(user = self.request.user, breveurl=breve_views.shortenURL())


class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = BookmarkDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Bookmark.objects.all()


class ClickDetailVeiw(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ClickDetailSerializer
    queryset = Click.objects.all()

class ClickViewSet(viewsets.ModelViewSet):
    
    queryset = Click.objects.all() # list all the books
    serializer_class = ClickDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) # prevents a user to see the post form if they are not authenticated
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
