# -*- coding: utf-8 -*-

import requests
import re
import demjson
import json
import setmenu
import time



def getuserlist(accesstoken,next_openid):
   url = 'https://api.weixin.qq.com/cgi-bin/user/get'

   params = {'access_token':accesstoken,
            'next_openid':next_openid
   }

   repsone = requests.get(url,params=params)

   result = json.loads(repsone.content)

   userlist = result['data']['openid']

   for i in userlist:
       getuserinfo(accesstoken,i)
       print '--------------------------------'

def getuserinfo(accesstoken,openid):
    url = 'https://api.weixin.qq.com/cgi-bin/user/info'

    params = {'access_token':accesstoken,
              'openid':openid
    }

    respone = requests.get(url,params=params)

    result = json.loads(respone.content)

    # print result['openid'] + " : " + result['nickname']
    for s in result:
        print s,result[s]


def sendinfo(token,openid):


    context = '猪饼子，你好！' + str(time.time())
    jsontext = {"touser": openid,
                "msgtype": "text",
                "text": {"content": context.strip()}}

    print jsontext

    postbody = json.dumps(jsontext,ensure_ascii=False)

    print postbody


    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'

    params = {'access_token':token}

    respone = requests.post(url,params=params,data=postbody)

    print respone.content

if __name__ == '__main__':
    appid = 'wx07d1254c491a8cc6'
    secret = '1f21ad347973a669afbde3513a6864d9'
    token = setmenu.getat(appid, secret)
    print token
    # next_openid = ''
    # getuserlist(token,next_openid)

    open_id = 'oScuNjo-KiUJqAUMBRkixTgcR3L8'
    # getuserinfo(token,open_id)
    # open_id = 'oScuNjp1EUWK3uDc_UAxt3SWaE8E'

    sendinfo(token,open_id)

