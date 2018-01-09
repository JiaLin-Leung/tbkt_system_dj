# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 21:56
# @作者  : 梁佳霖
# @文件名    : views.py
from tbkt_system_dj.utils import db

def login(username):

    sql = """
        SELECT * from auth_user where username = "%s"
    """ % username
    user = db.default.fetchone_dict(sql)
    user.user_id = user.id
    del user.id
    return user