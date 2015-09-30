#-*- coding:utf-8 -*-
import sys,urllib,urllib2,json

url='http://apis.baidu.com/rtbasia/dictionary_district/dictionary_district'

req = urllib2.Request(url)

req.add_header("apikey","c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)

content = resp.read()

print content.decode('utf-8')