from django.contrib import admin

# Register your models here.
from .models import *

class BookmarkAdmin(admin.ModelAdmin):
    fields=['url', 'description', 'tags', 'user', 'breveurl']
    list_display = ('url', 'description', 'created_at', 'last_updated')

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
