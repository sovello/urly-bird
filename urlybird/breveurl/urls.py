from django conf.urls import url
from django.views.generic import DetailView, ListView, View
from django.db.models import Bookmark

from . import views

#URLS
urlpatterns = [
    url(r'^/$', views.IndexView.as_view(), name='index'),
    url(r'home/$', views.UserView.as_view(), name='home_bookmark'),
    url(r'create/$', views.BookmarkCreateView.as_view(), name='create_bookmark'),
    url(r'update/(?P<pk>\d+/)$', views.BookmarkUpdateView.as_view(), name='update_bookmark'),
    url(r'login/$', 'django.contrib.auth.views.logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/home/'}),
]
