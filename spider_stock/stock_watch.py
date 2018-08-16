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
for one in all_report:
    #获取60个可用ip
    sid = one[1]
    #sid = '002415'
    link = 'http://d.10jqka.com.cn/v6/time/hs_%s/last.js'%(sid)
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js'%(sid)
    referer_link = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
    referer = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
    key = 'hs_%s'%(sid)

    #主要获取股票价格，是否涨停
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #content = stock_helper.getStockPrciePoints(referer_link)
    #content = stock_helper.getStockPrciePoints('http://stockpage.10jqka.com.cn/002415/')
    #content = stock_helper.getStockPrciePoints3('http://d.10jqka.com.cn/v2/realhead/hs_002415/last.js')
    link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/1500.js'%sid
    # link2 = 'http://d.10jqka.com.cn/v2/moneyflow/hs_002815/1500.js'
    content = stock_helper.getStockPrciePoints(link)
    #content = stock_helper.getStockPrciePoints(link2)
    content = stock_helper.getStockPrciePoints1('http://d.10jqka.com.cn/v2/realhead/hs_002815/last.js')
    content = stock_helper.getStockPrciePoints2('http://d.10jqka.com.cn/v2/fiverange/hs_002815/last.js')
    content = stock_helper.getStockPrciePoints3('http://d.10jqka.com.cn/v2/moneyflow/hs_002815/1500.js')
    # content = stock_helper.getStockPrciePoints(link)
    # content = stock_helper.getStockPrciePoints(link)
    #content = stock_helper.getStockPrciePoints('http://d.10jqka.com.cn/v2/realhead/hs_002415/last.js')
    print(content)
    time.sleep(random.uniform(1,2))
    continue
    if content is None:
        time.sleep(random.uniform(13, 15))
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
    # if is_stop == 1 :
    #     time.sleep(random.uniform(62, 65))
    #     continue
    # pre = float(all['pre'])#昨收
    # data_arr = all['data'].split(';')
    # name = all['name']
    # time.sleep(random.uniform(22, 25))
    # #获取大中小单
    # content = stock_helper.getStockMoneyPoints(money_link)
    #
    #
    # if content is None:
    #     time.sleep(random.uniform(1, 3))
    #     continue
    # arr = content.split('last(')
    # json_content = arr[1].strip(')')
    # json_content = json.loads(json_content)
    #
    # all = json_content[key]
    # money_data_arr = all['data'].split(';')
    #
    # #处理两组数据
    # k = 0
    # sql = 'insert into tan_stock_record values '
    # for one_point in data_arr:
    #     info = one_point.split(',')
    #     time_point = int(info[0])
    #     price = float(info[1])
    #     zdf = round((price-pre)/pre*100,2)
    #     volume = int(info[4])
    #     price = price
    #     volume = volume
    #     time_point = time_point
    #     date = today
    #     money_info = money_data_arr[k].split(',')
    #
    #     p1 = money_info[1]
    #     p2 = money_info[2]
    #     p3 = money_info[3]
    #     p4 = money_info[4]
    #     p5 = money_info[5]
    #     p6 = money_info[6]
    #     p7 = money_info[7]
    #     p8 = money_info[8]
    #     if(k==0):
    #         sql_str = '(null,"%s","%s",%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(name,sid,price,time_point,date,zdf,pre,volume,p1,p2,p3,p4,p5,p6,p7,p8)
    #     else:
    #         sql_str = ',(null,"%s","%s",%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(name, sid, price, time_point, date, zdf, pre, volume, p1, p2, p3, p4, p5, p6, p7, p8)
    #     sql += sql_str
    #     k +=1
    # print(sql)
    # stock_helper.insertStockRecord(sql)
    # time.sleep(random.uniform(1, 3))
    coords = [('AA', 'one'), ('AA', 'six'), ('BB', 'one'), ('BB', 'two'), ('BB', 'six')]