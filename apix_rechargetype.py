# -*- coding:utf-8 -*-
import urllib,urllib2,json

prov_id='v2043'
city_id='v2048'
url='http://p.apix.cn/apixlife/pay/utility/recharge_type?provid='+prov_id+'&cityid='+city_id



req = urllib2.Request(url)
req.add_header("apix-key","f19d00fa77834f2f589b0598568df900")

resp = urllib2.urlopen(req)
content = resp.read()
if content :
	results = json.loads(content,'utf-8')
	#print results
	if results['Code']==0:
		data = results['Data']
		#print type(data)
		for dk,dv in data.items():
			for dv_list in dv:
				print str(dv_list['PayProjectId']).encode('utf-8'),str(dv_list['PayProjectName']).encode('utf-8')
				
	else:
		print results['Msg'],results['Code']
