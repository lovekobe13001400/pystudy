#coding=utf-8
import urllib.request
#构建一个httphandler处理器对象，支持处理http请求
http_handler = urllib.request.HTTPHandler(debuglevel=1)

#构建一个httphandler对象，处理https请求
# http_handler = urllib2.HTTPSHandler()

#调用build_opener方法，创建支持处理Http请求的opener对象
opner = urllib.request.build_opener(http_handler)

request = urllib.request.Request("http://www.baidu.com")

#调用自定义opener对象的open(),发送request请求

response  = opner.open(request)

print(response.read())