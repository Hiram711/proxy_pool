# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting.py
   Description :   配置文件
   Author :        JHao
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""

# database config

DATABASES = {
    "default": {
        "TYPE": "MONGODB",  # TYPE SSDB/MONGODB if use redis, only modify the host port, the type should be SSDB
        "HOST": "127.0.0.1",
        "PORT": 37017,
        "NAME": "proxy",
        "USERNAME": "root",
        "PASSWORD": "root"

    }
}

# register the proxy getter function

PROXY_GETTER = [
    "freeProxyFirst",
    "freeProxySecond",
    # "freeProxyThird",
    "freeProxyFourth",
    "freeProxyFifth",
    # "freeProxySixth"
    "freeProxySeventh",
    # "freeProxyEight",
    # "freeProxyNinth",
    "freeProxyTen",
    "freeProxyEleven",
    "freeProxyTwelve",
    # foreign website, outside the wall
    "freeProxyWallFirst",
    "freeProxyWallSecond",
    "freeProxyWallThird"
]

# # API config http://127.0.0.1:5010

SERVER_API = {
    "HOST": "127.0.0.1",  # The ip specified which starting the web API
    "PORT": 5010  # port number to which the server listens to
}
