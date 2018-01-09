# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 16:50
# @作者  : 梁佳霖
# @文件名    : urls.py
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^user/login', views.login),              # 用户登录
]