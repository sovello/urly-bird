from django.db import models

# Create your models here.
class Bookmark(models.Model):

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Bookmarks'
        
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True, null=True)
    breveurl = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)

    
class Tag(models.Model):
    tags = models.CharField(max_length=255, blank=True, null=True)
    
