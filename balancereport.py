# -*- coding: utf-8 -*-

import getuinfo
import re

method = 'com.aop.method.historyaccquiry'
user_id = '18607106820'
config = {'billdate':'201512'}

result = getuinfo.getresult(method,user_id,**config)

res = result['billstr']


rs = re.findall("月固定费: (.*?);".decode('utf-8'),res,re.S)

print rs