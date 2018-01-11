# _*_ coding: utf-8 _*_
# @时间    : 2018/1/9 17:00
# @作者  : 梁佳霖
# @文件名    : __init__.py.py

import MySQLdb
from .db import Hub
from django.conf import settings

db = Hub(MySQLdb)
for alias, config in settings.DATABASES.items():
    db.add_pool(alias,
                host=config['HOST'],
                port=int(config.get('PORT', 3306)),
                user=config['USER'],
                passwd=config['PASSWORD'],
                db=config['NAME'],
                charset='utf8',
                autocommit=True,
                pool_size=settings.DB_POOL_SIZE,
                wait_timeout=settings.DB_WAIT_TIMEOUT,
    )
