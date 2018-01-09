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
