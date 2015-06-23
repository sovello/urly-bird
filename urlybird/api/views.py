#from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied

# Create your views here.
from api.serializers import BookmarkSerializer
from breveurl.models import Bookmark
from api.permissions import IsOwnerOrReadOnly
from breveurl import views as breve_views

class BookmarkViewSet(viewsets.ModelViewSet):
    """
    List all todos
    """
    queryset = Bookmark.objects.all() # list all the books
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) # prevents a user to see the post form if they are not authenticated
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user, breveurl=breve_views.shortenURL())


class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
