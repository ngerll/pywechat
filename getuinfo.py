# -*- coding: utf-8 -*-


import requests
import demjson
import getbody


def getuinfo(user_id):
    addconfig = {'method':'com.aop.method.realnamecheckqry','usernumber':user_id}
    params = getbody.getsign(**addconfig)

    url = 'http://132.38.0.86:9200/openservlet'

    respone = requests.get(url,params=params)

    context = respone.content


    result = demjson.decode(context)

    # for i in result:
    #     print i + result[i]

    return {'provincecode':result['provincecode'],
            'citycode':result['citycode'],
            'nettype':result['nettype'],
            'paytype':result['paytype']}




def getresult(method,user_id,**config):

    addconig = {'method':method,'usernumber':user_id}

    addconig.update(config)

    userinfo = getuinfo(user_id)
    addconig.update(userinfo)


    params = getbody.getsign(**addconig)

    url = 'http://132.38.0.86:9200/openservlet'

    respone = requests.get(url,params=params)

    context = respone.content

    result = demjson.decode(context)

    return result


if __name__ == '__main__':
    getuinfo('15671290038')

