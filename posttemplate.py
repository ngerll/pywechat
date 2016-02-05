# -*- coding: utf-8 -*-
import requests
import json
import setmenu



class Template:

    def __init__(self):
        appid = 'wxec80b374c3ace2a4'
        secret = '0dc774afff124f656d4983a1928fa276'
        self.appid = appid
        self.sercet = secret
        self.token = setmenu.getat(appid,secret)


    def getindustry(self):
        url = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template'
        param = {'access_token':self.token}


        datas = '''{"template_id_short":"TM00028"}'''

        respone = requests.post(url,params=param,data=datas)

        return respone.content


    def postinfo(self,template_id,datas):
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
        param = {'access_token':self.token}

        data = '''
                 {
                 "touser":"oheOMuFiBkdVAOyKI1hGC-NJNYBI",
                 "template_id":"''' + template_id + '''",
                 "url":"http://m.10010.com",
                 "data":''' + datas + '''
               } '''

        print data
        respone = requests.post(url,params=param,data=data)


        return respone


if __name__ == '__main__':

    temp = Template()
    # template_id = 'fKD3HuJjg35gJR2yB7RGH7jAQlLHA5174NiyDSpS1Fo'
    # datas = '''   {
    #                    "first": {
    #                        "value":"您的合约计划即将到期！",
    #                        "color":"#FF0033"
    #                    },
    #                    "keyword1":{
    #                        "value":"15607191388",
    #                        "color":"#FF0033"
    #                    },
    #                    "keyword2": {
    #                        "value":"全国iPhone6+ 128G预存话费送手机76元档(12个月)",
    #                        "color":"#FF0033"
    #                    },
    #                    "keyword3":{
    #                         "value":"2016年2月28日",
    #                         "color":"#FF0033"
    #                    },
    #                    "remark":{
    #                        "value":"您所办理的上述合约计划即将到期，您可以点击详情继续办理，谢谢！",
    #                        "color":"#0033FF"
    #                    }
    #               }'''

    template_id = 'dkJF2SOBp3x3o-mCT9XYBteeaFdGfKxazKkgbGztkrQ'

    datas = '''   {
                       "first": {
                           "value":"您的话费余额不足",
                           "color":"#FF0033"
                       },
                       "keyword1":{
                           "value":"15607191388",
                           "color":"#FF0033"
                       },
                       "keyword2": {
                           "value":"9.83 元",
                           "color":"#FF0033"
                       },
                       "remark":{
                           "value":"您的余额不足10元，请及时缴纳话费，谢谢！",
                           "color":"#0033FF"
                       }
                  }'''

    print temp.postinfo(template_id,datas)