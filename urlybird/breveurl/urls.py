from django.conf.urls import url
from django.views.generic import DetailView, ListView, View, TemplateView
from .models import Bookmark
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^qt/(?P<urlid>[a-zA-Z0-9]+)', views.takemethere, name="redirects"),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/$', views.UserView.as_view(), name='home_bookmark'),
    url(r'^create/$', views.BookmarkCreateView.as_view(), name='create_bookmark'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.BookmarkUpdateView.as_view(), name='update_bookmark'),
    url(r'^delete_bookmark/$', views.delete_bookmark, name='delete_bookmark'),
    url(r'^login/$', 'django.contrib.auth.views.logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/breveurl/'}),
    url(r'^click/', include('click.urls')),

]
