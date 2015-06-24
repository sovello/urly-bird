from rest_framework import serializers

from breveurl.models import Bookmark
from click.models import Click

class BookmarkListSerializer(serializers.HyperlinkedModelSerializer):
    clicks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="click-detail")
    bookmark = serializers.URLField(source="url")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="bookmark-detail") # the view name here is name of the URL in the urls.py
    
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'url', 'bookmark',  'description', 'breveurl', 'clicks')


class BookmarkDetailSerializer(serializers.HyperlinkedModelSerializer):

    bookmark = serializers.URLField(source="url")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="bookmark-detail") # the view name here is name of the URL in the urls.py

    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'url', 'bookmark', 'description', 'breveurl', 'created_at', 'clicks')


class ClickDetailSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Click
        fields = ('id', 'url', 'bookmark', 'accessed_at', 'ip_address', 'user')
