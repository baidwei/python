# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

#上海满友信息科技有限公司(企业)
#1069三网合一短信接口
#试用套餐:20次:免费
url = 'http://apis.baidu.com/021manyou_bao/manyoubao/manyousdk?mobile=15326036086&msg=%E9%AA%8C%E8%AF%81%E7%A0%81%EF%BC%9A1234%E3%80%90%E6%BB%A1%E5%8F%8B%E7%A7%91%E6%8A%80%E3%80%91'


req = urllib2.Request(url)

req.add_header("apikey", "c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)