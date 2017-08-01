#!/usr/bin/python env

__author__ = 'wangxiaodong'
# project name:MyDjango
#   file name:urls.py
#   auther:wangxiaodong
#   create date:2017/7/24 15:11
#   change auther:
#   change date:
#   version:V1.0
#   using environment:Fusioninsight HD U60C200
#   python version:python 2.6.6
#   usage:

from django.conf.urls import url
#get from MyDjango.urls
from django.contrib import admin

from . import views

app_name = 'wxd'
urlpatterns = [
    #get from MyDjango.urls
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name='result'),
    # ex: /wxd/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]