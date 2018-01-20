define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./apidoc/main.js",
    "group": "C__Interesting_tbkt_system_dj_apidoc_main_js",
    "groupTitle": "C__Interesting_tbkt_system_dj_apidoc_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "C__Interesting_tbkt_system_dj_doc_main_js",
    "groupTitle": "C__Interesting_tbkt_system_dj_doc_main_js",
    "name": ""
  },
  {
    "type": "POST",
    "url": "/account/admin/create",
    "title": "[管理员]创建用户",
    "group": "account",
    "parameter": {
      "examples": [
        {
          "title": "表单请求",
          "content": "\"real_name\":\"孟祥\"\n\"level_type\":3\n\"phone_number\":\"13556666964\"",
          "type": "params"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回",
          "content": "{\n    \"message\": \"创建成功!\",\n    \"next\": \"\",\n    \"data\": {\n        \"username\": \"mengxiang\",\n        \"phone_number\": \"13556666964\",\n        \"level_type\": 3,\n        \"user_id\": 85,\n        \"creat_time\": 1515641851,\n        \"real_name\": \"孟祥\",\n        \"password\": \"mengxiangqazwsx\"\n    },\n    \"response\": \"ok\",\n    \"error\": \"\"\n}",
          "type": "json"
        },
        {
          "title": "失败返回",
          "content": "{\n    \"message\": \"\",\n    \"next\": \"\",\n    \"data\": null,\n    \"response\": \"fail\",\n    \"error\": \"该用户已存在\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./tbkt_system_dj/account/views.py",
    "groupTitle": "account",
    "name": "PostAccountAdminCreate"
  },
  {
    "type": "POST",
    "url": "/account/user/login",
    "title": "[用户]登录",
    "group": "account",
    "parameter": {
      "examples": [
        {
          "title": "表单请求",
          "content": "\"username\":\"liangjialin\"\n\"password\":\"111111\"",
          "type": "params"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回",
          "content": "{\n    \"message\": \"\",\n    \"next\": \"\",\n    \"data\": {\n        \"username\": \"liangjialin\",\n        \"phone_number\": \"13556666964\",\n        \"level_type\": 3,\n        \"user_id\": 81,\n        \"creat_time\": 1515638660,\n        \"real_name\": \"梁佳霖\",\n        \"password\": \"liangjialinqazwsx\"\n    },\n    \"response\": \"ok\",\n    \"error\": \"\"\n}",
          "type": "json"
        },
        {
          "title": "失败返回",
          "content": "{\n    \"error\": \"\",\n    \"message\": \"查无此人\",\n    \"next\": \"\",\n    \"response\": \"fail\"\n}",
          "type": "json"
        },
        {
          "title": "失败返回",
          "content": "{\n    \"error\": \"\",\n    \"message\": \"密码错误\",\n    \"next\": \"\",\n    \"response\": \"fail\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./tbkt_system_dj/account/views.py",
    "groupTitle": "account",
    "name": "PostAccountUserLogin"
  },
  {
    "type": "POST",
    "url": "/ticket/get_all_ticket_by_type",
    "title": "[工单]根据type获取某个用户工单情况",
    "group": "ticket",
    "parameter": {
      "examples": [
        {
          "title": "表单请求",
          "content": "\"user_id\":\"4\"\n\"status\":\"0\"  '0 未完成  1 已完成 2全部'\n\"type\":\"0\"  \"0 全部状态 1 响应状态 2 响应超时 3 响应错误 4 SQL慢查询 5 APP错误\"",
          "type": "params"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回",
          "content": "{\n        \"message\": \"\",\n        \"next\": \"\",\n        \"data\": [\n            {\n                \"count\": null,\n                \"status\": 0,\n                \"domain\": \"hd.m.jxtbkt.cn\",\n                \"url\": \"/apple-touch-icon.png\",\n                \"status_code\": null,\n                \"from_user_name\": null,\n                \"end_time\": 20180103,\n                \"begin_time\": 20180102,\n                \"from_user_id\": 1,  \n                \"id\": 4,\n                \"type\": 1,  '1 响应状态 2 响应超时 3 响应错误 4 SQL慢查询 5 APP错误'\n                \"add_time\": \"0000-00-\"\n            }\n        ],\n        \"response\": \"ok\",\n        \"error\": \"\"\n    }",
          "type": "json"
        },
        {
          "title": "成功返回",
          "content": "{\n    \"message\": \"\",\n    \"next\": \"\",\n    \"data\": [],\n    \"response\": \"ok\",\n    \"error\": \"\"\n}",
          "type": "json"
        },
        {
          "title": "失败返回",
          "content": "{\n    \"message\": \"\",\n    \"next\": \"\",\n    \"data\": null,\n    \"response\": \"fail\",\n    \"error\": \"缺少参数user_id\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./tbkt_system_dj/ticket/ticket.py",
    "groupTitle": "ticket",
    "name": "PostTicketGet_all_ticket_by_type"
  }
] });
