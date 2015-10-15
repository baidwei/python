#-*- coding:utf-8 -*-
import urllib,urllib2,json

city='北京'
startaddr='锦秀嘉苑'
endaddr='阿尔泰'
url='http://apis.baidu.com/apistore/bustransport/bustransfer?city='+city+'&start_addr='+startaddr+'&end_addr='+endaddr

req= urllib2.Request(url)
req.add_header('apikey','c9e78e76a5b0f37f90ba746ede713387')

resp = urllib2.urlopen(req)
content = resp.read()
if content:
	results = json.loads(content,'utf-8')
	if results['errNum']==0:
		#print type(results['retData'])
		for k,v in results['retData'].items():
			print str(k).encode('utf-8'),str(v).encode('utf-8')
			if k =='result':
				print str(v).encode('utf-8')
	else:
		print results['errNum'],results['retMsg']

