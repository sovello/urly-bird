from django.db import models
from django.contrib.auth.models import User
from breveurl.models import Bookmark

# Create your models here.
class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark, related_name="clicks")
    accessed_at = models.DateTimeField(null=True, blank=True)
    ip_address = models.CharField(max_length = 255)
    user = models.ForeignKey(User)
    
