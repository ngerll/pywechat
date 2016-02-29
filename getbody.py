# -*- coding: utf-8 -*-

import hashlib
import base64
import datetime
import hmac

def getsign(**config):

    securet = 'swUiuzms+bAqgNOhTaJAyaTFVdAhGaG2aPCUJ0o72P/dSFj8aRbFDOXjPTBB5oja9plfRNWgTKP1OFWBF2F85A=='

    param = {'appkey':'com.aop.app.hbmicrochannel',
             'timestamp':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             'apptx':'tamp' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
             }

    param.update(config)




    keys = param.keys()
    keys.sort()
    sign_tmp = ''

    for key in keys:
        sign_tmp = sign_tmp + key + '$' + str(param[key]) + '$'

    sign_tmp =  sign_tmp[:-1]

    skey = base64.b64decode(securet)

    mac = hmac.new(skey,sign_tmp)
    sign = base64.b64encode(mac.digest())

    signd = {'sign':sign}
    param.update(signd)

    return param


if __name__ == '__main__':
    addconfig = {'method':'com.aop.method.realnamecheckqry','usernumber':'15607191388'}

    print getsign(**addconfig)







