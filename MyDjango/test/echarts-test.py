#!/usr/bin/python env

__author__ = 'wangxiaodong'
# project name:MyDjango
#   file name:echarts-test
#   auther:wangxiaodong
#   create date:2017/7/24 0:29
#   change auther:
#   change date:
#   version:V1.0
#   using environment:Fusioninsight HD U60C200
#   python version:python 2.6.6
#   usage:

from echarts import Echart, Legend, Bar, Axis

chart = Echart('GDP', 'This is a fake chart')
chart.use(Bar('China', [2, 3, 4, 5]))
chart.use(Legend(['GDP']))
chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))