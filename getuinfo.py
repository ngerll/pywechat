# -*- coding: utf-8 -*-


import requests
import demjson
import getbody


def getuinfo(user_id):
    addconfig = {'method':'com.aop.method.realnamecheckqry','usernumber':user_id}
    params = getbody.getsign(**addconfig)

    url = 'http://211.94.67.94:8001/openservlet'

    respone = requests.get(url,params=params)

    context = respone.content


    result = demjson.decode(context)

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

    url = 'http://211.94.67.94:8001/openservlet'

    respone = requests.get(url,params=params)

    context = respone.content

    result = demjson.decode(context)

    return result

getuinfo('05545311913')

