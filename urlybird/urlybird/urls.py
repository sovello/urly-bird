"""urlybird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static # to include media files
#from breveurl.views import views
from rest_framework import routers
from api import views as api_views
from userapi import views as userapi_views

router = routers.DefaultRouter()
router.register(r'bookmarkapi', api_views.BookmarkViewSet)
router.register(r'userapi', userapi_views.UserViewSet)

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^breveurl/', include('breveurl.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'bookmark/(?P<pk>\d+)', api_views.BookmarkDetailView.as_view()),
    url(r'user/(?P<pk>\d+)', userapi_views.UserDetailView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
