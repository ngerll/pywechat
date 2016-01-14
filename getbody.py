import requests
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
    sgin_tmp = ''

    for key in keys:
        sgin_tmp = sgin_tmp + key + '$' + param[key]

    sgin_str = securet +'$' + sgin_tmp + '$' + securet
    print sgin_str
    sign_m = hmac.new(sgin_str)
    sign_md5 = sign_m.digest()
    print sign_md5

    sign = base64.b64encode(sign_md5)

    print sign

    signd = {'sign':sign}
    param.update(signd)

    return param



# if __name__ == '__main__':
#     addconfig = {'method':'com.aop.method.realnamecheckqry','usernumber':'15607191388'}
#
#     print getsign(**addconfig)







