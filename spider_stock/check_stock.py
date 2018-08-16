#coding=utf-8
'''
获取每天个股的数据(部分股票)
'''
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
import time
from mysql.proxy_api import proxy_list
import random
#构建2个代理ip
helper = MysqlHelper()
#请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc',
    'Referer':'http://stockpage.10jqka.com.cn/HQ_v4.html'
}
today = datetime.now().strftime('%Y-%m-%d')
now_time = int(time.time())
dif_now_time = int(time.time()) - 65
sql = "select * from tan_stock where is_watch=1"
all_report = helper.get_all(sql)

#准备一个需要的ip
nullproxy_handler = urllib.request.ProxyHandler({})
for one in all_report:
    sid = one[1]
    link = 'http://stockpage.10jqka.com.cn/%s/'% (sid)
    request = urllib.request.Request(link, headers=headers)
    opener = urllib.request.build_opener(nullproxy_handler)
    response = opener.open(request)
    print(response)



