# -*- coding: utf-8 -*-

import getuinfo



def getflow(user_id):

    method = 'com.aop.method.mobilenetdata'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)


    if result['respcode'] == '0000':
        flowinf =  result['flowinf']

        detailenddate = result['detailenddate'] #截止

        for s in flowinf:
            packageusedflow = s['packageusedflow'] #主套餐已用
            packageleavingsflow = s['packageleavingsflow'] #主套餐剩余
            packageflow = float(packageusedflow) + float(packageleavingsflow) #总量
            print detailenddate,packageusedflow,packageleavingsflow,packageflow

    else:
        pass

def getpackage(user_id):
    method = 'com.aop.method.combospare'
    config = {'billdate':'201601'}

    result = getuinfo.getresult(method,user_id,**config)
    rinfo = result['feepolicyaddupinfo']

    for i in range(len(rinfo)):
        print '---------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]

def getleavepackagedata(user_id):
    method = 'com.aop.method.leavepackagedata'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    rinfo =  result['flowinf']

    for i in range(len(rinfo)):
        print '-------------------'
        for s in rinfo[i]:
            print s + " : " + rinfo[i][s]


def getresourceremainqry(user_id):
    method = 'com.aop.method.resourceremainqry'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)


    resinfo =  result['resourceinfo']
    dinfo = resinfo[0]
    rinfo = dinfo['detailresourceinfo'][1]

    for s in rinfo:
        print s + " : " + rinfo[s]

if __name__ == '__main__':
    pass
    # getflow('13036128806')
    # getpackage('18607106820')
    # getleavepackagedata('15623092667')
    # getresourceremainqry('18607106820')
