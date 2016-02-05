# -*- coding: utf-8 -*-

import requests


def getinfo():
    url = 'http://wap.10010hb.net/weixin/mvc/apaas/custinfo'

    head = {'Host': 'wap.10010hb.net',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-cn',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'http://wap.10010hb.net',
            'Content-Length': '98',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.3.13 NetType/WIFI Language/zh_CN',
            'Referer': 'http://wap.10010hb.net/weixin/wap/hb_offical_acct/templates/acctQuery/myInfo.jsp',
            'Cookie': 'JSESSIONID='}

    # datas = '''{"SERIAL_NUMBER":"18518051163","PROV_CODE":"071","CITY_CODE":"710","NET_TYPE":"11","PAY_TYPE":"2"}'''
    datas = '''{"SERIAL_NUMBER":"18608661606","PROV_CODE":"071","CITY_CODE":"710","NET_TYPE":"11","PAY_TYPE":"2","BILL_DATE":"201601"}'''

    respone = requests.post(url,headers=head,data=datas)

    print respone.content


if __name__ == '__main__':
    getinfo()