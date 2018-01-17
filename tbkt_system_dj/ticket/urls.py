# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 16:50
# @作者  : 梁佳霖
# @文件名    : urls.py
from django.conf.urls import url
import ticket

urlpatterns = [
    url(r'^get_all_ticket', ticket.get_all_ticket),              # 用户工单列表
]