from rest_framework import serializers

from breveurl.models import Bookmark



class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    bookmark_url = serializers.CharField(source="url")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'url', 'bookmark_url', 'description', 'breveurl', 'created_at')
