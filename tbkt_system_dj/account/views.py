# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 16:55
# @作者  : 梁佳霖
# @文件名    : ticket.py

from tbkt_system_dj.utils import ajax
from tbkt_system_dj.utils import db
from tbkt_system_dj.account.common import views
from xpinyin import Pinyin
import json
import time

def login(request):

    """
    @api {POST} /account/user/login [用户]登录
    @apiGroup account
    @apiSuccessExample {json} 成功返回
    {
        "data": {
            "creat_time": 111111,
            "id": 1,
            "level_type": 1,
            "password": "111111",
            "phone_number": 1513617071,
            "real_name": "liangjialin",
            "username": "liangjialin"
        },
        "error": "",
        "message": "",
        "next": "",
        "response": "ok"
    }
    @apiSuccessExample {json} 失败返回
    {
        "error": "",
        "message": "查无此人",
        "next": "",
        "response": "fail"
    }
    @apiSuccessExample {json} 失败返回
    {
        "error": "",
        "message": "密码错误",
        "next": "",
        "response": "fail"
    }
    """
    user = json.loads(request.body)
    username = user.get("username")
    password = user.get("password")
    if not username:
        return ajax.jsonp_fail(request, message='请输入用户名')
    if not password:
        return ajax.jsonp_fail(request, message='请输入密码')
    user = views.login(username)
    if not user:
        return ajax.jsonp_fail(request, message="查无此人")
    password_real = user.password  # 利用用户名在数据库找到的人,并查到这个人的密码
    if password_real == password:
        return ajax.jsonp_ok(request,user)
    else:
        return ajax.jsonp_fail(request, message="密码错误")


def create(request):

    """
    管理员创建用户
    :param request: 
    :return: 
    """
    user = json.loads(request.body)
    level_type = user.get("level_type") # 用户等级
    real_name = user.get("real_name")  # 用户真实姓名
    phone_number = user.get("phone_number")  # 用户手机号码
    pinyin = Pinyin()
    password = 111111
    creat_time = time.time()
    username = pinyin.get_pinyin(real_name, "")  # 用户用户名(根据真实姓名转换的拼音)
    if not username:
        return ajax.jsonp_fail(request, message='少参数:level_type')
    if not real_name:
        return ajax.jsonp_fail(request, message='少参数:real_name')
    if not phone_number:
        return ajax.jsonp_fail(request, message='少参数:phone_number')
    data = views.create(username,password,real_name,phone_number,creat_time,level_type)
    if data:
        return ajax.jsonp_ok(request, data)










