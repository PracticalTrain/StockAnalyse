__author__ = 'jjzhu'
from django.conf.urls import url
from . import views
app_name = 'history'
urlpatterns = [
    url(r'^detail/$', views.detail, name='detail'),
]
