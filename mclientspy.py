# -*- coding: utf-8 -*-

import requests
import binascii

def getinfo():
    url = 'http://short.weixin.qq.com/cgi-bin/mmbiz-bin/bizattr/bizattrsync'

    head = {'User-Agent': 'MicroMessenger Client'}

    datas = '''v7ZfFgMNEQRQeeEKAggBYEggQLF/qNzHfACzCHBwAAGn27ieBAEAkII+bgEA3f/pT57QikeDAVWMVCwlA5s+q7WLHzRk336AMuRKsalmrHEA+pui8Ncl20sNtTPC17taI6fBy+dn2b4edVR5M05HGm37jGjiX7+qzw1d/hcEoTY0QBCWYkouaQqC/zNpAVDC8E36fywH7WUZcnFX9hZS1OTN/GjqxFTBARFSGTY='''

    respone = requests.post(url,headers=head,data=datas)

    print binascii.b2a_hex(respone.content)


if __name__ == '__main__':
    getinfo()



