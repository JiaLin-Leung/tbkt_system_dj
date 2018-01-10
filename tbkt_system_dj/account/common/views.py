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
    sql = """
        INSERT INTO `ticket_main`.`auth_user` (`username`, `password`, `real_name`, `phone_number`, `creat_time`, `level_type`) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
    """ % (username,password,real_name,phone_number,creat_time,level_type)
    data = db.default.fetchone_dict(sql2)
    return data