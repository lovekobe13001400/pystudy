#coding=utf-8
'''
获取每天版块的数据
'''
import sys
sys.path.append('..')
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
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
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
}
#all_plate_sql = "select * from tan_plate"
sid_str = '885378,885745,885790,885423,885312,885362,885728,885452'
all_plate_sql = "select * from tan_plate where sid in (%s)"%(sid_str)
all_paltes = helper.get_all(all_plate_sql)
# print(all_paltes)
# params = {'name': '阿里巴巴概念', 'sid': 'aa', 'price': 1109.905, 'time_point': 930.0, 'date': '2018-06-14', 'zdf': -0.54, 'pre': 1115.926, 'volume': 5475532}
# print(params)
# sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
# helper.insert(sql,params)

for one in all_paltes:

    link = 'http://d.10jqka.com.cn/v4/time/bk_%s/last.js'%(one[1])
    referer = 'http://q.10jqka.com.cn/gn/detail/code/%s/'%(one[3])
    temp_hedaers = headers
    temp_hedaers['Referer'] = referer
    request = urllib.request.Request(link, headers=temp_hedaers)
    response = opener.open(request)
    content = response.read().decode()
    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)
    key = 'bk_%s'%(one[1])
    all = json_content[key]
    pre = float(all['pre'])#昨收
    data_arr = all['data'].split(';')
    name = all['name']
    sid = one[1]
    today = datetime.now().strftime('%Y-%m-%d')

    for one_point in data_arr:
        info = one_point.split(',')
        time_point = int(info[0])
        price = float(info[1])
        zdf = round((price-pre)/pre*100,2)
        volume = int(info[4])
        params = {"name": name, "sid": sid, "price": price,"time_point":time_point, "date": today,"zdf":zdf,"pre":pre,"volume":volume}
        sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
        print(params)
        helper.insert(sql,params)
        #print(helper)

    time.sleep(60)  # 休眠1秒
# link = 'http://d.10jqka.com.cn/v4/time/bk_885751/last.js'
# request = urllib.request.Request(link,headers=headers)
#
# response = opener.open(request)
# content = response.read().decode()
# arr = content.split('last(')
# json_content = arr[1].strip(')')
# json_content = json.loads(json_content)
# all = json_content['bk_885751']
# pre = float(all['pre'])#昨收
# data_arr = all['data'].split(';')
# name = all['name']
# sid = 00
# today = datetime.now().strftime('%Y-%m-%d')
# for one_point in data_arr:
#     info = one_point.split(',')
#     time_point = float(info[0])
#     price = float(info[1])
#     zdf = round((price-pre)/pre*100,2)
#     volume = int(info[4])
#     params = {"name": name, "sid": sid, "price": price,"time_point":time_point, "date": today,"zdf":zdf,"pre":pre,"volume":volume}
#
#     sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
#     helper.insert(sql,params)
#     #print(helper)
#     break

