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
  }
] });
