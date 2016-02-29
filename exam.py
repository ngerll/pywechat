# -*- coding: utf-8 -*-


import os
import time
import requests
import re

def getUUID():
    global uuid

    url = 'https://login.weixin.qq.com/jslogin'
    params = {
        'appid': 'wx782c26e4c19acffb',
        'fun': 'new',
        'lang': 'zh_CN',
        '_': int(time.time()),
    }

    request = requests.get(url,params=params)
    response = request.content
    print response





if __name__ == '__main__':
    getUUID()