# -*- coding: utf-8 -*-

import getuinfo
import re
from flask import *


app=Flask(__name__)

@app.route('/<user_id>')
def index(user_id):

    method = 'com.aop.method.mobilenetdata'
    config = {}

    result = getuinfo.getresult(method,user_id,**config)

    userflow = {}

    usernumber = {'user_id':user_id}

    userflow.update(usernumber)

    if result['respcode'] == '0000':
        flowinf =  result['flowinf']

        detailenddate = {'detailenddate':result['detailenddate']} #截止
        userflow.update(detailenddate)


        for s in flowinf:
            packageusedflow = s['packageusedflow'] #主套餐已用
            packageleavingsflow = s['packageleavingsflow'] #主套餐剩余
            packageflow = float(packageusedflow) + float(packageleavingsflow) #总量

            packflow = {'packageusedflow':packageusedflow,
                        'packageleavingsflow':packageleavingsflow,
                        'packageflow':packageflow}
            userflow.update(packflow)
    else:
        pass
    return render_template('hb_index.html',userflow=userflow)

if __name__ == '__main__':
    app.run(debug=True)


