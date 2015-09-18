#encoding=utf-8
import sys, urllib, urllib2, json

appkey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx' #您申请到的数据的APPKEY
url = 'http://apis.juhe.cn/ip/ip2addr' #数据API请求URL
paramsData = {'ip': "www.juhe.cn", 'key': appkey} #需要传递的参数
params = urllib.urlencode(paramsData)

req = urllib2.Request(url, params)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    result = json.loads(content, 'utf-8')
    error_code = result['error_code']
    if(error_code == 0):
        data = result['result'] #接口返回结果数据
        print(data)
    else:
        errorinfo = str(error_code)+":"+result['reason'] #返回不成功，错误码:原因
        print(errorinfo)