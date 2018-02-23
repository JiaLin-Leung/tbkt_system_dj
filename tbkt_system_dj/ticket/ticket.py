# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 22:07
# @作者  : 梁佳霖
# @文件名    : ticket.py

from tbkt_system_dj.ticket.common import ticket as common
from tbkt_system_dj.utils import ajax

def get_all_ticket_by_type(request):
    """
    @api {POST} /ticket/get_all_ticket_by_type [工单]根据type获取某个用户工单情况
    @apiGroup ticket
    @apiParamExample {params} 表单请求
"user_id":"4"
	"status":"0"  '0 未完成  1 已完成 2全部'
	"type":"0"  "0 全部状态 1 响应状态 2 响应超时 3 响应错误 4 SQL慢查询 5 APP错误"
	@apiSuccessExample {json} 成功返回
	{
        "message": "",
        "next": "",
        "data": [
            {
                "count": null,
                "status": 0,
                "domain": "hd.m.jxtbkt.cn",
                "url": "/apple-touch-icon.png",
                "status_code": null,
                "from_user_name": null,
                "end_time": 20180103,
                "begin_time": 20180102,
                "from_user_id": 1,  
                "id": 4,
                "type": 1,  '1 响应状态 2 响应超时 3 响应错误 4 SQL慢查询 5 APP错误'
                "add_time": "0000-00-"
            }
        ],
        "response": "ok",
        "error": ""
    }
    @apiSuccessExample {json} 成功返回
    {
        "message": "",
        "next": "",
        "data": [],
        "response": "ok",
        "error": ""
    }
    @apiSuccessExample {json} 失败返回
    {
        "message": "",
        "next": "",
        "data": null,
        "response": "fail",
        "error": "缺少参数user_id"
    }
    """
    user_id = request.POST.get("user_id")  # 用户user_id
    status = request.POST.get("status")  # 单条任务完成情况
    type = request.POST.get("type") # 0 全部状态 1 响应状态 2 响应超时 3 响应错误 4 SQL慢查询 5 APP错误

    if not user_id:
        return ajax.jsonp_fail(request,"缺少参数user_id")
    if not type:
        return ajax.jsonp_fail(request, "缺少参数type")
    user_tircket = common.get_all_ticket_by_type(user_id,status,type)  # 获取该用户工单
    if user_tircket != -1:
        return ajax.jsonp_ok(request,user_tircket)
    else:
        return ajax.jsonp_ok(request, [])
