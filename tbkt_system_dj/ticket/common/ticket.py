# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 21:56
# @作者  : 梁佳霖
# @文件名    : ticket.py
from tbkt_system_dj.utils import db

def get_all_ticket_by_type(user_id,status,type):

    status = int(status)
    type = int(type)
    if status == 2 and type == 0:
        sql = """
                    SELECT type,count,status,domain,status_code,url,from_user_name,end_time,begin_time,from_user_id
                    ,id,add_time from ticket_system.error_task where user_id = %s;
                """ % (user_id)
        user_tircket = db.default.fetchall_dict(sql)
    elif status == 2 and type != 0:
        sql = """
                            SELECT type,count,status,domain,status_code,url,from_user_name,end_time,begin_time,from_user_id
                            ,id,add_time from ticket_system.error_task where user_id = %s AND type = %s;
                        """ % (user_id,type)
        user_tircket = db.default.fetchall_dict(sql)
    else:
        sql = """
                    SELECT type,count,status,domain,status_code,url,from_user_name,end_time,begin_time,from_user_id
                    ,id,add_time from ticket_system.error_task where user_id = %s AND status = %s AND type = %s;
                """ % (user_id,status,type)
        user_tircket = db.default.fetchall_dict(sql)
    if not user_tircket:
        return -1
    return user_tircket