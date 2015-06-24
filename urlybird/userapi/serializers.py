from rest_framework import serializers
from django.contrib.auth.models import User
from breveurl.models import Bookmark

class UserSerializer(serializers.ModelSerializer):       
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name="bookmark-detail", read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'bookmarks')
