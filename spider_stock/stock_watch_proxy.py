#coding=utf-8
'''
获取每天个股的数据(部分股票)
'''
import sys
sys.path.append('..')
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
from spider_stock.StockHelper import StockHelper
import time
from mysql.proxy_api import proxy_list
import socket
import random
#构建2个代理ip
stock_helper = StockHelper()

today = datetime.now().strftime('%Y-%m-%d')
sql = "select * from tan_stock where is_watch=1"
all_report = stock_helper.getWatchStock()

#准备一个需要的ip
# while 1:
#     url1 = 'http://d.10jqka.com.cn/v2/realhead/hs_002415/last.js'
#     referer = 'http://stockpage.10jqka.com.cn/realHead_v2.html'
#     url2 = 'http://d.10jqka.com.cn/v6/time/hs_002415/last.js'

for one in all_report:
    #获取60个可用ip
    sid = one[1]
    link = 'http://d.10jqka.com.cn/v6/time/hs_%s/last.js'%(sid)
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js'%(sid)
    referer = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
    key = 'hs_%s'%(sid)
    ip_api_url = 'http://api.ip.data5u.com/dynamic/get.html?order=709b9f8c8a98b6e74a57e70e3e3544fa&json=1&sep=3'
    ip_info = stock_helper.getStockPrciePoints(ip_api_url)
    ip_info = json.loads(ip_info)
    ip = ip_info['data'][0]['ip']
    port = ip_info['data'][0]['port']

    handler_obj = {}
    handler_obj['https'] = ip +':'+str(port)
    print(handler_obj)

    #主要获取股票价格，是否涨停
    content = stock_helper.getStockPrciePoints(link,handler_obj)
    #exit()
    if content is None:
        #time.sleep(random.uniform(62, 65))
        time.sleep(5)
        continue
    arr = content.split('last(')

    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)
    all = json_content[key]
    is_stop = all['stop']
    is_open = all['open']

    #不开市
    # if is_open == 0:
    #     break
    #停牌
    if is_stop == 1 :
        time.sleep(random.uniform(5, 6))
        continue
    pre = float(all['pre'])#昨收
    data_arr = all['data'].split(';')
    name = all['name']
    #time.sleep(random.uniform(62, 65))
    #获取大中小单
    time.sleep(6)
    ip_info = stock_helper.getStockPrciePoints(ip_api_url)
    ip_info = json.loads(ip_info)
    ip = ip_info['data'][0]['ip']
    port = ip_info['data'][0]['port']
    content = stock_helper.getStockMoneyPoints(money_link,handler_obj)
    if content is None:
        time.sleep(6)
        continue
    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)

    all = json_content[key]
    money_data_arr = all['data'].split(';')

    #处理两组数据
    k = 0
    sql = 'insert into tan_stock_record values '
    for one_point in data_arr:
        info = one_point.split(',')
        time_point = int(info[0])
        price = float(info[1])
        zdf = round((price-pre)/pre*100,2)
        volume = int(info[4])
        price = price
        volume = volume
        time_point = time_point
        date = today
        money_info = money_data_arr[k].split(',')
        p1 = money_info[1]
        p2 = money_info[2]
        p3 = money_info[3]
        p4 = money_info[4]
        p5 = money_info[5]
        p6 = money_info[6]
        p7 = money_info[7]
        p8 = money_info[8]
        if(k==0):
            sql_str = '(null,"%s","%s",%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(name,sid,price,time_point,date,zdf,pre,volume,p1,p2,p3,p4,p5,p6,p7,p8)
        else:
            sql_str = ',(null,"%s","%s",%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(name, sid, price, time_point, date, zdf, pre, volume, p1, p2, p3, p4, p5, p6, p7, p8)
        sql += sql_str
        k +=1
    print(sql)
    #stock_helper.insertStockRecord(sql)
    time.sleep(6)