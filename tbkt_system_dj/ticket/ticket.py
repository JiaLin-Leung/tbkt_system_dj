# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 22:07
# @作者  : 梁佳霖
# @文件名    : ticket.py

from tbkt_system_dj.ticket.common import ticket as common
from tbkt_system_dj.utils import ajax

def get_all_ticket(request):
    user_id = request.POST.get("user_id")  # 用户ID
    status = request.POST.get("status") # 单条任务完成情况
    if not user_id:
        return ajax.jsonp_fail(request,"缺少参数user_id")
    user_tircket = common.get_all_ticket(user_id,status)  # 获取该用户工单
    if user_tircket != -1:
        return ajax.jsonp_ok(request,user_tircket)
    else:
        return ajax.jsonp_fail(request, "暂无工单")
