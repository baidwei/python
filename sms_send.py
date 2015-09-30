#-*- coding:utf-8 -*-
import sys,urllib,urllib2,json

url='http://apis.baidu.com/chinasofti/chinasofti/chinasofti?regcode=PAPH-CRM-0100-RAQMEU&pwd=ef47aa0aa6cae84cb8e22f40f8b25159&phone=15326036086&CONTENT==%E4%B8%AD%E8%BD%AF%E5%9B%BD%E9%99%85%E7%99%BE%E5%BA%A6%E6%8E%A8%E5%B9%BF%E9%AA%8C%E8%AF%81%E7%A0%81%EF%BC%9A6868'

req= urllib2.Request(url)

req.add_header("apikey","c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)
content = resp.read()
if content:
	print content