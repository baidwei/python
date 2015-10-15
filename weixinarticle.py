# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json,types
keyword='内蒙古音乐之声'
url = 'http://apis.baidu.com/antelope/wechat/article?keyword='+keyword+'&pageNo=1'


req = urllib2.Request(url)

req.add_header("apikey", "c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    results = json.loads(content,'utf-8')
    #print results
    if results['status']=='200':
    	for r in results['list']:
    		for rk,rv in r.items():
    			#print type(rv)
    			if type(rv)==types.DictType:
    				for kxk,kxv in rv.items():
    					print str(kxk).encode('utf-8')+':'+str(kxv).encode('utf-8')
    			else:
    				print str(rk).encode('utf-8')+':'+str(rv).encode('utf-8')
