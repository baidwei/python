#-*- coding:utf-8 -*-
import base64
f = open(r'C:\Users\user\Desktop\IMG_20151012_152543.jpg','rb')
ls_f = base64.b64encode(f.read())
print ls_f
f.close()