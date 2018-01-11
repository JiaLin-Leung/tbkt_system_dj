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

def create(username,password,real_name,phone_number,creat_time,level_type):
    """
        db.default.execute(sql)
    """
    user = db.default.auth_user.get(username=username)
    if user:
        return -1
    user_id = db.default.auth_user.create(username=username,
                                       password=password,
                                       real_name=real_name,
                                       phone_number=phone_number,
                                       creat_time=creat_time,
                                       level_type=level_type)
    return user_id

def person_info(user_id):
    """
    根据user_id找到用户全部信息
    :param user_id: 
    :return: 
    """
    person = db.default.auth_user.get(id = user_id)
    person.user_id = person.id
    del person.id
    return person

