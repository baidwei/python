#-*- coding:utf-8 -*-
import sys,urllib,urllib2,json

say_text = "内蒙古呼和浩特市" 

#参数text：要进行urlencode编码
#ctp：客户端类型选择，web 端填写 1
#per:发音人选择，取值 0-1 ；0 为女声，1 为男声
url = 'http://apis.baidu.com/apistore/baidutts/tts?'+'text='+say_text+'&ctp=1&per=1'

req = urllib2.Request(url)

req.add_header("apikey","c9e78e76a5b0f37f90ba746ede713387")

resp = urllib2.urlopen(req)

content = resp.read()

if content:
	results=json.loads(content,'utf-8')
	if results['errNum'] ==0:
		#响应的retData：进行base64的语音文件，格式为mp3
		print results['retData']
		html = open('index.html','w')
		html.write("""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<audio controls="controls" autobuffer="autobuffer" autoplay="autoplay" src="data:audio/mp3;base64,"""+results['retData']+"""
"/>
 </audio>
</body>
</html>
			""")

	else:
		print 'Error Number:'+str(results['errNum'])+',Error Msg:'+results['retMsg']


#输出到html文件中，然后通过浏览器访问，可以播放音频	
'''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<audio controls="controls" autobuffer="autobuffer" autoplay="autoplay" src="data:audio/mp3;base64,//MoxAAKuEFph0kQAK6pgAgCCKMVtpBQMMoEGXNGjCwPjgQcUcT///////////z5d8EIYreXfDCAaFsyi1bPd7Pe3QAb1+rj//MoxBAOwGaRv5sqAtP8sQIZOQnUKG/36sMnffAhN112+U5nTqnN8upvX7kd/Wb06b9X3ff+j+j/1/47FCZtpRhRrGX5pb0u//MoxBAQMbqkAdooAKiqK1mXyii7r8eZijN/+8j+////////2U8TEgIND4fDgcBAIn2/WOcJAQDAfED/9yIIKSW0FOAWEEFK//MoxAoOUH7dHgKMLgJk7+QklkIQ//o8YmCHZtCv1oB8c00SE5845rP/UXYjdlHVqu/7EruaHhIBLP9i6gDypbLQk5R/Zh4H//MoxAsPkbrZv0coAiD4RReZXYoLhr6rsEQR/vKjFT6IVP9RJ/3mDyt1///8xjFCQe8FmxKCpb//2RsO/6nwk6rbUQFgVOCp//MoxAcOESKwAYlAADZYvP//M29WtJHvXHMonu+/Cptlx9XLxqEYLqkdYTg1HGeCC6SCP+v/7XM8hFej/+UqAqmAGEXKFAEH//MoxAkPARKtk8UQAEVMcPHUt9mqjMn5l+ZOqvQjSykI5WRmRGEiI8INDk42wgkGv//2FxOET5CAjYnYyEiUHBFa5ZIlKLw///MoxAgOoWbaXDBHSvJEg+w2RBYeM95OlIEvf1s1v1rjmrU5MkUTX8amPSJBpfY0dj1jIFrGV//9jK06+3+imhv///WQGfH3//MoxAgO+MLeUAYYDQKkdA3OD4TTq3ueugdyyWn3hIOScGpaHsrgMHsdwFqwPlcjiQWzPBLXrixedfsIwEAE9hN/nwMvrclI//MoxAcMqPLMwFMSOw6erebHMpLa6dk8sGR01CB8oGTxPNhgeebNgWUbQpro0nrlyMQKoTzk6V66Ezk5Ey4UADJYBxcwoJY3//MoxA8NAML6PgLGGh70A+tbeVs60FZ8B29Uz6wkt4MKAAPVgJ5zr5nes01owUR//aoNOMPAYACZ65kZEq4gIRUJiREezbjc//MoxBYMgNbV/gJMDLq96JR55i1NiVriVPaxPyTEnqkQ0r+r///+devGCVolAH0TRLXJVwa0mN1pd7QGrhVUKR2CXK2l0xLl//MoxB8NMNbM3hmHBmDhIfcd8nrF77v//3BUAhAOhpFK9KYJuSQkuAD8AMGAgLVmY/6rN6qUuzeql9VfjNwwIU0FpVwi//////MoxCUNAM7KXgDGAv8FSwNA0dLRK4SuBp5YGq0nIlZQABC/qqplcr/u+q3+JUpt/kqgwdVMQU1FMy45OS41VVVVVVVVVVVV//MoxCwGGAYOWAhGA1VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy45OS41VVVVVVVVVVVV//MoxE4AAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy45OS41VVVVVVVVVVVV//MoxIkAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//MoxMQAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//MoxMQAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//MoxMQAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"/>
 </audio>
</body>
</html>
'''