#coding=utf-8
import urllib.request
url = "http://www.baidu.com/s"
word = {"wd":"lol"}
word = urllib.parse.urlencode(word)
newurl = url + '?' + word
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#请求对象
request = urllib.request.Request(newurl,headers=headers)
#请求
res = urllib.request.urlopen(request)
#获取页面信息
page = res.read().decode('utf-8');
fo = open("test.txt", "w",encoding='utf-8')
fo.write(page)
