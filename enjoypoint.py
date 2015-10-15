#-*-coding:utf-8 -*-
import sys,urllib,urllib2,json

keyword="金桥"			#搜索关键词，如百度大厦，苏州街
cityName="呼和浩特"			#cityName: 搜索的城市名,
singlepagenum="1"   #单页上所获取的数据的数目
pagenum="1"    		#获取指定页面的数据
output="json"		#输出的数据格式，默认为xml格式


url='http://apis.baidu.com/apistore/point/search?keyWord='+keyword+'&cityName='+cityName+'&number='+singlepagenum+'&page='+pagenum+'&output='+output+''
req = urllib2.Request(url)
req.add_header("apikey","c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)
content = resp.read()
if content:
	results=json.loads(content,'utf-8')
	if results['status'] =="Success":
		#响应的retData：进行base64的语音文件，格式为mp3
		print '热点记录总数:'+str(results['total']).encode('utf-8')
		print '结果返回数量:'+str(results['count']).encode('utf-8')
		pLists = results['pointList']
		print pLists
		print type(pLists)	
		for pList in pLists:
			if type(pList)=='dict':
				print 'dict'

			else:
				print str(pList).encode('utf-8')
			'''
		for pList in pLists:
			print str(pList['name']).encode('utf-8')
			print str(pList['district']).encode('utf-8')
			additionInfos = pList['additionalInformation']
			#print additionInfos
			#print type(additionInfos)
			for k,v in additionInfos.items():
				print k,str(v).encode('utf-8') 
				'''
	else:
		print results['status']
