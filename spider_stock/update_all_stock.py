#coding=utf-8
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
from lxml import etree
from func import is_float
import random
import time
#构建2个代理ip
httpproxy_handler = urllib.request.ProxyHandler({"http" : "117.90.3.190:9000"})
nullproxy_handler = urllib.request.ProxyHandler({})
helper = MysqlHelper()

#定义一个代理开关
proySwitch = False

if(proySwitch):
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; refreshStat=off; user=MDp3YWtlcmN5OjpOb25lOjUwMDozNzU4ODE2MTg6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjI1Ojo6MzY1ODgxNjE4OjE1MjkyNDE5MzI6OjoxNDgwNTk0ODYwOjMxNTI2ODowOjEzYmMxYTU3ZTQ5MjRmZDdhNGYzNGZlYzY4OTNjMjE5MzpkZWZhdWx0XzI6MA%3D%3D; userid=365881618; u_name=wakercy; escapename=wakercy; ticket=30158138cccbcb9c7c8fa673af7ce4ce; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1528942207,1529030502,1529232862,1529287863; Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1528942207,1529030502,1529232862,1529287863; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528942207,1529030502,1529232862,1529287863; historystock=300666%7C*%7C600121%7C*%7C300345%7C*%7C600546%7C*%7C300139; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1529299647; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1529299647; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1529302328; searchGuide=sg; v=AruatnLfZOXyJlhR0Fz0uI3lSpQgEMd2yTySya14ldPTCNVANeBfYtn0Iw6-',
    'Referer':'http://data.10jqka.com.cn/market/zdfph/'
}

page = 56
max_page = 1000
while(1):
    page+=1
    if(page>=max_page):
        break
    link = 'http://data.10jqka.com.cn/market/zdfph/field/zdf/order/desc/page/%s/ajax/1/'%(page)
    request = urllib.request.Request(link, headers=headers)
    response = opener.open(request)
    html = response.read()
    html =  html.decode('gbk')
    selector = etree.HTML(html)
    item = {}
    for sel in selector.xpath('//table/tbody/tr'):
        item['sid'] = str(sel.xpath('td[2]/a/text()')[0])
        item['sname'] = str(sel.xpath('td[3]/a/text()')[0])
        item['is_watch'] = 0
        sql = 'insert ignore into tan_stock values(null,%(sid)s,%(sname)s,%(is_watch)s)'
        helper.insert(sql,item)
    page_info = selector.xpath('//span[@class="page_info"]/text()')
    page_arr = page_info[0].split('/')
    page_max = page_arr[1]
    time.sleep(random.uniform(62, 65))
