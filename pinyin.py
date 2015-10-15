#-*- coding:utf-8 -*-
import urllib,urllib2,sys,json

w='欢迎使用python'
url =' http://a.apix.cn/fore/sinaapp/pinyin/api.php?w='+w

req = urllib2.Request(url)
req.add_header('apix-key','bdc06b4705cd41dd77a25e82c369754f')

resp = urllib2.urlopen(req)
content = resp.read()

if content:
	results = json.loads(content,'utf-8')
	if results['status'] == 1:
		print results['result']
	else:
		print results['result']
