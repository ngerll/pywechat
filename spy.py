# -*- coding: utf-8 -*-

import requests


def getinfo():
    url = 'http://wap.10010hb.net/weixin/mvc/apaas/custinfo'

    head = {'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'2',
            'Content-Type':'application/json; charset=UTF-8',
            'Cookie':'JSESSIONID=',
            'Host':'wap.10010hb.net',
            'Origin':'http://wap.10010hb.net',
            'Referer':'http://wap.10010hb.net/weixin/wap/hb_offical_acct/templates/acctQuery/myInfo.jsp',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.3.13 NetType/WIFI Language/zh_CN',
            'X-Requested-With':'XMLHttpRequest'}

    datas = '''{"SERIAL_NUMBER":"18607181557","PROV_CODE":"071","CITY_CODE":"710","NET_TYPE":"02","PAY_TYPE":"2"}'''

    respone = requests.post(url,headers=head,data=datas)

    print respone.content


if __name__ == '__main__':
    getinfo()