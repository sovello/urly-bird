from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stats/year/(?P<year>[0-9]{4})/', views.stats, name='stats'),
    url(r'^stats/map/(?P<bookmark>[0-9]+)$', views.stats_map, name='stats_map'),    
]
