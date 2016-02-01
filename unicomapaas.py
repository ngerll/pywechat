# -*- coding: utf-8 -*-

import getuinfo
import datetime



def getflow(user_id):

    method = 'com.aop.method.mobilenetdata'  #上网流量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

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

    for i in range(len(rinfo)):
        print '---------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]

def getleavepackagedata(user_id):
    method = 'com.aop.method.leavepackagedata'  #套餐余量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)


    rinfo =  result['flowinf']

    for i in range(len(rinfo)):
        print '-------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


def getresourceremainqry(user_id):
    method = 'com.aop.method.resourceremainqry' #资源余量查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)


    resinfo =  result['resourceinfo']
    dinfo = resinfo[0]
    rinfo = dinfo['detailresourceinfo'][1]

    for s in rinfo:
        print s + " : " + rinfo[s]

def getuserinfo(user_id):
    method = 'com.aop.method.custinfo' #客户信息查询
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    for s in result:
        print s,result[s]


def getcontractperiodqry(user_id):  #合约计划
    method = 'com.aop.method.contractperiodqry'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    rinfo =  result['activityinfo']

    for i in range(len(rinfo)):
        print '------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


def getphonenetflowdetail(user_id): #移动手机上网记录查询
    method = 'com.aop.method.phonenetflowdetail'
    config = {'proctime':datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
              'querytype':'02',
              'begindate':'20160128000000',
              'enddate':datetime.datetime.now().strftime("%Y%m%d%H%M%S")}

    result = getuinfo.getresult(method,user_id,**config)



    rinfo = result['record']

    for i in range(len(rinfo)):
        print '-'*20
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


if __name__ == '__main__':
    getflow('18607146513')   #上网流量查询
    # getpackage('18607106820')  #4G套餐余量查询
    # getleavepackagedata('15607191388') #套餐余量查询
    # getresourceremainqry('18607146513') #资源余量查询
    # getuserinfo('18607106820') #客户信息查询
    # getcontractperiodqry('18696185833') #合约计划
    # getphonenetflowdetail('15607191388') #移动手机上网记录查询