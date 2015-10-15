#-*-coding:utf-8 -*-
import urllib,urllib2,json

city="呼和浩特"
station="凯元广场"
url = 'http://apis.baidu.com/apistore/bustransport/busstations?city='+city+'&station='+station
req = urllib2.Request(url)
req.add_header("apikey","c9e78e76a5b0f37f90ba746ede713387")

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