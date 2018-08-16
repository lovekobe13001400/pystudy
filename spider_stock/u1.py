#from urllib import request
#你好
import urllib.request
res = urllib.request.urlopen('http://www.baidu.com')
html = res.read()
print(html)