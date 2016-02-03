# -*- coding: utf-8 -*-
import requests
import json
import setmenu


def getindustry(token):
    url = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template'
    param = {'access_token':token}


    datas = '''{"template_id_short":"TM00028"}'''

    respone = requests.post(url,params=param,data=datas)

    return respone.content


def postinfo(token):
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
    param = {'access_token':token}

    data = '''
             {
           "touser":"oheOMuFiBkdVAOyKI1hGC-NJNYBI",
           "template_id":"y99fu8FO8dvkWKV6ArcPEm6VrNBZXVitK0WjrmZo6fY",
           "url":"http://m.10010.com",
           "data":{
                   "first": {
                       "value":"您好，您的流量不足！",
                       "color":"#173177"
                   },
                   "time":{
                       "value":"2016年2月3日12时",
                       "color":"#173177"
                   },
                   "yiyong": {
                       "value":"1100Mb",
                       "color":"#173177"
                   },
                   "taocan remainder":{
                        "value":"50Mb",
                        "color":"#173177"
                   },
                   "remark":{
                       "value":"您可以点击详情购买流量包，谢谢！",
                       "color":"#173177"
                   }
           }
       }
            '''
    respone = requests.post(url,params=param,data=data)

    return respone


if __name__ == '__main__':
    appid = 'wxec80b374c3ace2a4'
    secret = '0dc774afff124f656d4983a1928fa276'
    token = setmenu.getat(appid,secret)

    postinfo(token)