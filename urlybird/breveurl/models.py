from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True, null=True)
    breveurl = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_accessed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.url)

    class Meta:
        verbose_name_plural = 'Bookmarks'
        ordering = ['-created_at']
        
    @property
    def short_url(self):
        return 'http://localhost:8000/breveurl/qt/'


class BookmarkAnonymous(models.Model):
    randid = models.IntegerField(default= 1)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_accessed = models.DateTimeField()
    
class Tag(models.Model):
    tags = models.CharField(max_length=255, blank=True, null=True)
    
