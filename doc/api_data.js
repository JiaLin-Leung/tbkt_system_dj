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
          "content": "{\n    \"message\": \"\",\n    \"next\": \"\",\n    \"data\": {\n        \"username\": \"gaohaifei\",\n        \"phone_number\": \"13556666964\",\n        \"level_type\": 3,\n        \"creat_time\": 1515639376,\n        \"real_name\": \"高海飞\",\n        \"password\": \"gaohaifeiqazwsx\",\n        \"id\": 82\n    },\n    \"response\": \"ok\",\n    \"error\": \"\"\n}",
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
          "content": "{\n    \"data\": {\n        \"creat_time\": 111111,\n        \"id\": 1,\n        \"level_type\": 1,\n        \"password\": \"111111\",\n        \"phone_number\": 1513617071,\n        \"real_name\": \"liangjialin\",\n        \"username\": \"liangjialin\"\n    },\n    \"error\": \"\",\n    \"message\": \"\",\n    \"next\": \"\",\n    \"response\": \"ok\"\n}",
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
