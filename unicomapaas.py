# -*- coding: utf-8 -*-

import getuinfo
import datetime



def getflow(user_id):

    method = 'com.aop.method.mobilenetdata'  #上网流量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in result:
        print s,result[s]


    # if result['respcode'] == '0000':
    #     flowinf =  result['flowinf']
    #
    #     detailenddate = result['detailenddate'] #截止
    #
    #     for s in flowinf:
    #         packageusedflow = s['packageusedflow'] #主套餐已用
    #         packageleavingsflow = s['packageleavingsflow'] #主套餐剩余
    #         packageflow = float(packageusedflow) + float(packageleavingsflow) #总量
    #         print detailenddate,packageusedflow,packageleavingsflow,packageflow
    #
    # else:
    #     pass

def getpackage(user_id):
    method = 'com.aop.method.combospare'  #4G套餐余量查询
    config = {'billdate':'201601'}

    result = getuinfo.getresult(method,user_id,**config)
    rinfo = result['feepolicyaddupinfo']

    print result

    for i in range(len(rinfo)):
        print '---------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]

def getleavepackagedata(user_id):
    method = 'com.aop.method.leavepackagedata'  #套餐余量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    rinfo =  result['flowinf']

    for i in range(len(rinfo)):
        print '-------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


def getresourceremainqry(user_id):
    method = 'com.aop.method.resourceremainqry' #资源余量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    resinfo =  result['resourceinfo']
    dinfo = resinfo[0]
    rinfo = dinfo['detailresourceinfo'][1]

    for s in rinfo:
        print s + " : " + rinfo[s]

def getuserinfo(user_id):
    method = 'com.aop.method.custinfo' #客户信息查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in result:
        print s,result[s]


def getcontractperiodqry(user_id):  #合约计划
    method = 'com.aop.method.contractperiodqry'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)
    print result

    rinfo =  result['activityinfo']

    for i in range(len(rinfo)):
        print '------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


def getphonenetflowdetail(user_id): #移动手机上网记录查询
    method = 'com.aop.method.phonenetflowdetail'
    config = {'proctime':datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
              'querytype':'02',
              'begindate':'20160229000000',
              'enddate':datetime.datetime.now().strftime("%Y%m%d%H%M%S")}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    rinfo = result['record']

    for i in range(len(rinfo)):
        print '-'*20
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]

def getprodpackage(user_id) : #产品套餐查询
    method = 'com.aop.method.prodpackage'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)
    print result

    for s in result['produinf']:
        for i in s :
            print i + s[i]

def getscoreexpendrecord(user_id): #积分消费记录
    method = 'com.aop.method.scoreexpendrecord'
    config = {'begindate': '20151201',
              'enddate' : '20151231'}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in  result['record']:
        for i in s :
            print i + " : " + s[i]

def getscorerecord(user_id): #积分产生记录
    method = 'com.aop.method.scorerecord'
    config = {'begindate': '20151201',
              'enddate' : '20151231'}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in  result['record']:
        for i in s :
            print i + " : " + s[i]

def setpasswdchange(user_id): #修改密码
    method = 'com.aop.method.passwdchange'
    config = {'passwdchangetype' :'00',
              'oldpasswd':'868629',
              'newpasswd':'782911'}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def getbalancereport(user_id): #统一余额播报
    method = 'com.aop.method.balancereport'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result

def gethistoryaccquiry(user_id): #历史账单查询
    method = 'com.aop.method.historyaccquiry'
    config = {'billdate':'201601'}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def getcurrentfeequiry(user_id): #当月话费查询
    method = 'com.aop.method.currentfeequiry'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def onlineauthentication(user_id): #在线身份验证
    method = 'com.aop.method.onlineauthentication'
    config = {'password':'782911'}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def getpaymentrecord(user_id): #交费记录查询
    method = 'com.aop.method.paymentrecord'
    config = {'begindate':'20151001',
              'enddate':'20160228'}

    result = getuinfo.getresult(method,user_id,**config)

    print result

def getscore(user_id): #积分查询
    method = 'com.aop.method.score'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def getmobileinfo(user_id): #移动业务信息查询
    method = 'com.aop.method.mobileinfo'
    config = {'mobilebusinesstype':'00',
              'businesstype':'0'}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in result['record']:
        for i in s:
            print i + " : " + s[i]



def mobilebusichange(user_id): #移动业务变更
    method = 'com.aop.method.mobilebusichange'
    config = {'mobilebusinesstype':'00',
              'featcode':'13022000020',
              'servicestatus':'00',
              'busiorder':'BUSI001602291305595800109428',
              'businesstype':'0'}

    result = getuinfo.getresult(method,user_id,**config)

    print result


def getbusiacceptrecord(user_id): #业务受理记录查询
    method = 'com.aop.method.busiacceptrecord'
    config = {'begindate':'20151001',
              'enddate':'20160101'}

    result = getuinfo.getresult(method,user_id,**config)

    print result

    for s in result['record']:
        for i in s :
            print i + ' : ' + s[i]



if __name__ == '__main__':
    # getflow('18607146513')   #上网流量查询
    # getpackage('18607106820')  #4G套餐余量查询
    # getleavepackagedata('15607191388') #套餐余量查询
    # getresourceremainqry('18607146513') #资源余量查询
    # getuserinfo('18607106820') #客户信息查询
    # getcontractperiodqry('18696185833') #合约计划
    # getphonenetflowdetail('15607191388') #移动手机上网记录查询
    # getprodpackage('18607106820') #产品套餐
    # getscoreexpendrecord('18672397563') #积分消费记录
    # getscorerecord('18607106820') #积分产生记录
    # setpasswdchange('15607191388') #修改密码
    # getbalancereport('15607191388') #统一余额播报
    # gethistoryaccquiry('15607191388') #历史账单查询
    # getcurrentfeequiry('18607106820') #当月话费查询
    # onlineauthentication('15607191388') #在线身份验证
    # getpaymentrecord('18607106820') #交费记录查询
    # getscore('18607106820') #积分查询
    # getmobileinfo('15607191388') #移动业务查询
    # mobilebusichange('15607191388') #移动业务办理
    getbusiacceptrecord('15607191388')
