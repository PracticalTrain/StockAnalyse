__author__ = 'jjzhu'
from django.conf.urls import url
from . import views
app_name = 'news'
urlpatterns = [

    url(r'^p/(?P<page_num>[0-9]+)/$', views.get_news_by_pages, name='page'),
    url(r'^d/(?P<news_id>[0-9]+)/$', views.detail, name='detail'),
]