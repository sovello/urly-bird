from django.contrib import admin

# Register your models here.
from .models import Click

class ClickAdmin(admin.ModelAdmin):
    fields=['bookmark', 'user', 'ip_address']
    list_display = ('bookmark', 'accessed_at', 'user', 'ip_address')

admin.site.register(Click, ClickAdmin)

