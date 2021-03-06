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
from werkzeug.security import generate_password_hash, check_password_hash

def login(request):

    """
    @api {POST} /account/user/login [用户]登录
    @apiGroup account
    @apiParamExample {params} 表单请求
"username":"liangjialin"
	"password":"111111"
	@apiSuccessExample {json} 成功返回
    {
        "message": "",
        "next": "",
        "data": {
            "username": "liangjialin",
            "phone_number": "13556666964",
            "level_type": 3,
            "user_id": 81,
            "creat_time": 1515638660,
            "real_name": "梁佳霖",
            "password": "liangjialinqazwsx"
        },
        "response": "ok",
        "error": ""
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
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not username:
        return ajax.jsonp_fail(request, message='请输入用户名')
    if not password:
        return ajax.jsonp_fail(request, message='请输入密码')
    user = views.login(username)
    print 111111111,user
    if not user or user == -1:
        return ajax.jsonp_fail(request, message="查无此人")
    if check_password_hash(user.password_hash,password):
        return ajax.jsonp_ok(request,user)
    else:
        return ajax.jsonp_fail(request, message="密码错误")


def create(request):

    """
    @api {POST} /account/admin/create [管理员]创建用户
    @apiGroup account
    @apiParamExample {params} 表单请求
"real_name":"孟祥"
	"level_type":3
	"phone_number":"13556666964"
    @apiSuccessExample {json} 成功返回
    {
        "message": "创建成功!",
        "next": "",
        "data": {
            "username": "mengxiang",
            "phone_number": "13556666964",
            "level_type": 3,
            "user_id": 85,
            "creat_time": 1515641851,
            "real_name": "孟祥",
            "password": "mengxiangqazwsx"
        },
        "response": "ok",
        "error": ""
    }
    @apiSuccessExample {json} 失败返回
    {
        "message": "",
        "next": "",
        "data": null,
        "response": "fail",
        "error": "该用户已存在"
    }
    """
    user = json.loads(request.body)
    level_type = user.get("level_type") # 用户等级
    real_name = user.get("real_name")  # 用户真实姓名
    phone_number = int(user.get("phone_number"))  # 用户手机号码
    pinyin = Pinyin()
    creat_time = time.time()
    username = pinyin.get_pinyin(real_name, "")  # 用户用户名(根据真实姓名转换的拼音)
    password = username+"qazwsx"
    if not username:
        return ajax.jsonp_fail(request, message='少参数:level_type')
    if not real_name:
        return ajax.jsonp_fail(request, message='少参数:real_name')
    if not phone_number:
        return ajax.jsonp_fail(request, message='少参数:phone_number')
    user_id = views.create(username,password,real_name,phone_number,creat_time,level_type)
    if user_id != -1:
        person = views.person_info(user_id)
        if person:
            return ajax.jsonp_ok(request,person,message="创建成功!")
    else:
        return ajax.jsonp_fail(request,message="该用户已存在")









