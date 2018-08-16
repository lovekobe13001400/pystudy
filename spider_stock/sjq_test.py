#coding=utf-8
'''
获取每天版块的数据
'''
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
from mysql.proxy_api import proxy_list
import time
import socket
import redis
#连接redis服务器
#redis_res = redis.StrictRedis(host='localhost',port=6379,password='',db=1)

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
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
}
link = "http://www.tan66.com/"
link = 'http://stockpage.10jqka.com.cn/002415/'
#url =  'http://47.75.51.71:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'
url =  'http://localhost:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'
sql = "select * from ip order by success_num desc"
all_ip = helper.get_all(sql)
for one_ip in all_ip:
    ip = one_ip[1]
    port = one_ip[2]
    scheme = one_ip[3]
    handler_obj = {}
    value = ip + ':' + port
    handler_obj[scheme] = value
    try:
        request = urllib.request.Request(link)
        print(handler_obj)
        exit()
        httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
        socket.setdefaulttimeout(10)
        opener = urllib.request.build_opener(httpproxy_handler)
        response = opener.open(request)
        print('yes')
        # #
        # sql_exists = "select * from ip where ip='%s'"%(ip);
        # ip_exists = helper.get_one(sql_exists)
        # if ip_exists is None:
        #     sql = 'insert ignore into ip values(null,%(ip)s,%(port)s,%(scheme)s,%(success_num)s,%(fail_num)s)'
        #     params = {'ip':ip,'port':port,'scheme':scheme,'success_num':1,'fail_num':0}
        #     #ip是否存在，存在更新，失败录入
        #     helper.insert(sql, params)
        # else:
        #     sql = 'update ip set success_num=success_num+1 where ip="%s"'%(ip);
        #     helper.update(sql)
        #成功ip
    except Exception as e:
        #print(e)
        #sql = 'insert into ip values(null,%(ip)s,%(success_num)s,%(fail_num)s)'
        # sql = "delete from ip where ip='%s'"%(ip)
        # helper.delete(sql)
        print('no')

#直接从数据库中获取60个，一个个去爬取，一旦失败，重新去数据库获取，再写一个脚本，验证所有success>2的ip是否可用
