# -*- coding: utf-8 -*-

import requests
import json
import urllib2
import demjson

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def getat(appid,secret):
    url = 'https://api.weixin.qq.com/cgi-bin/token'

    params = {'grant_type':'client_credential',
              'appid':appid,
              'secret':secret

    }

    respone = requests.get(url,params=params)

    result = json.loads(respone.content)

    return result['access_token']


def getmenujson(token):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/get'

    params = {'access_token':token}

    respone = requests.get(url,params=params)

    return respone.content


def delemenu(token):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/delete'

    params = {'access_token':token}

    respone = requests.get(url,params=params)

    return respone.content


def setmenu(token):
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % token




    with open('E://baiduyun//wx_menu//menu_hblt.json','r') as jsonf:
        context = ''

        for line in jsonf.readlines():
            line = line.strip()
            context += line


    respone = requests.post(url,data=context)

    return respone.content


if __name__ == '__main__':
    appid = 'wxec80b374c3ace2a4'
    secret = '0dc774afff124f656d4983a1928fa276'
    token = getat(appid,secret)
    # print getmenujson(token)

    # print delemenu(token)

    print setmenu(token)