#coding=utf-8
import urllib.request
import ssl
#忽略ssl
ssl._create_default_https_context=ssl._create_unverified_context
url = "https://www.12306.cn/mormhweb/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)

print(response.read())
