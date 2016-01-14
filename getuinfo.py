import requests
import demjson
import getbody


def getuinfo():
    addconfig = {'method':'com.aop.method.realnamecheckqry','usernumber':'15607191388'}
    params = getbody.getsign(**addconfig)
    print params

    url = 'http://211.94.67.94:8001/openservlet'

    respone = requests.get(url,params=params)

    print respone.url
    context = respone.content

    print context

getuinfo()