# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

mnc="0"
sid="13824" #SID系统识别码
nid="0" #NID网络识别码
cellid="291" #基站号
ishex='0'  #cellid是否16进制，ishex=0表示10进制，ishex=1表示16进制。默认为0
url_tel = 'http://apis.baidu.com/apix/apix_station_data/apix_telecom?sid=13824&nid=0&cellid=291&ishex=0'
url_tel1 = 'http://apis.baidu.com/apix/apix_station_data/apix_telecom?sid=14120&nid=0&cellid=2ab2&ishex=1'
url_template = 'http://apis.baidu.com/apix/apix_station_data/apix_telecom'
params={
    'sid':sid,
    'nid':nid,
    'cellid':cellid,
    'ishex':ishex
}
uparams=urllib.urlencode(params)

url_template=url_template+'?'+uparams

url_mob = 'http://apis.baidu.com/apix/apix_station_data/apix_mobi?mnc=0&lac=4286&cellid=1361&ishex=0'
#2ab2
#14120
print "运营商代码 mnc=",mnc,"\n小区代码 lac=4286 \n基站号 cellid=1361 \ncellid是否16进制 ishex=0"

print "============================"
req = urllib2.Request(url_template)

req.add_header("apikey", "c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    #print(content)
    result = json.loads(content,'utf-8')
    err_code= result['code']
    if err_code=="0": #0:成功;1:数据不存在;2:传入的参数值错误;3:传入的参数名称错误.
    	result_data=result['data']
    	
    	print "省份或直辖市:",str(result_data['prov']).encode('utf-8')
    	print "城市 :",str(result_data['city']).encode('utf-8')
    	print "县/区:",str(result_data['dist']).encode('utf-8')
    	print "乡镇街道:",str(result_data['town']).encode('utf-8')
    	print "道路 :",str(result_data['street']).encode('utf-8')
    	print "地址描述:",str(result_data['addr']).encode('utf-8'),"门牌号:",str(result_data['number'])
    	print "基站精度（米）:",str(result_data['acc'])
    	print "经度:",str(result_data['lon'])
    	print "纬度:",str(result_data['lat'])
    
    else:
    	print "error code:",err_code," 0:成功;1.数据不存在;2.传入的参数值错误;3.传入的参数名称错误"

