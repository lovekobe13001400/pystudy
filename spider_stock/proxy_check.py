#coding=utf-8
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
import time
import socket

#构建2个代理ip
httpproxy_handler = urllib.request.ProxyHandler({"http" : "114.99.27.5:18118"})
nullproxy_handler = urllib.request.ProxyHandler({})
helper = MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
#定义一个代理开关
proySwitch = False



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
}
all_plate_sql = "select * from tan_proxy";
all_proxy = helper.get_all(all_plate_sql)
# print(all_paltes)
# params = {'name': '阿里巴巴概念', 'sid': 'aa', 'price': 1109.905, 'time_point': 930.0, 'date': '2018-06-14', 'zdf': -0.54, 'pre': 1115.926, 'volume': 5475532}
# print(params)
# sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
# helper.insert(sql,params)

for one in all_proxy:

    ip = "%s%s%s"%(one[1],':',one[2])
    httpproxy_handler = urllib.request.ProxyHandler({"http": ip})
    opener = urllib.request.build_opener(httpproxy_handler)
    link = 'http://ls.duowan.com/'
    temp_hedaers = headers
    socket.setdefaulttimeout(3)
    request = urllib.request.Request(link, headers=temp_hedaers)

    try:
        response = opener.open(request)
        sql = 'update tan_proxy set is_ok=1';
        helper.update(sql)
        print(ip)
        print('ok')
    except Exception as error:
        #直接删除这个代理
        #print('wrong')
        pass

