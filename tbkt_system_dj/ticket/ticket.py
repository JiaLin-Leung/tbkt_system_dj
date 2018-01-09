# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 22:07
# @作者  : 梁佳霖
# @文件名    : ticket.py

def get_all_ticket(requst):

    user_id = request.POST.get("user_id")  # 用户ID
    real_name = request.POST.get("real_name") # 用户真实姓名
    level_type = request.POST.get("level_type") # 用户等级