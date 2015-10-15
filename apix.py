#-*- coding:utf-8 -*-
import sys,urllib,urllib2,json,types

prov_name=u'内蒙古'

url ='http://p.apix.cn/apixlife/pay/utility/query_province'

req = urllib2.Request(url)
req.add_header("apix-key","f19d00fa77834f2f589b0598568df900")

resp = urllib2.urlopen(req)
content = resp.read()
if content :
	results = json.loads(content,'utf-8')

	for res_k,res_v in results.items():
		#print res_k,res_v
	
		if type(res_v) ==types.DictType:
			for res_v_k,res_v_v in res_v.items():
				#print res_v_k,res_v_v
				#print type(res_v_v)
				if type(res_v_v)==types.DictType:
					for pid,pname in res_v_v.items():
						print pid,pname
				elif type(res_v_v)==types.ListType:
					for res_list in res_v_v:
						#print res_list
						#print str(res_list['ProvinceId']).encode('utf-8'),str(res_list['ProvinceName']).encode('utf-8')
						if str(res_list['ProvinceName']).encode('utf-8')==str(prov_name).encode('utf-8'):
							print str(res_list['ProvinceId']).encode('utf-8')
						else:
							pass
					print "",
		else:
			pass
	#print type(results)
