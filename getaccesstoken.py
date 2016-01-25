# -*- coding: utf-8 -*-

import requests
import json


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

    print respone.url

    print respone.content




if __name__ == '__main__':
    appid = 'wx07d1254c491a8cc6'
    secret = '1f21ad347973a669afbde3513a6864d9'
    token = getat(appid,secret)
    print token
    getmenujson(token)