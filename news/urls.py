__author__ = 'jjzhu'
from django.conf.urls import url
from . import views
app_name = 'news'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<news_id>[0-9]+)/$', views.detail, name='detail'),
]