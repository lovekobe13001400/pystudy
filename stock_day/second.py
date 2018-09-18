#1.及时爬取股票信息(2分钟1只股票)
#2.爬取好，算好斜率，直接存（满足条件才存），存记录，有可能早上存一条，晚上存一条
#3.查看历史斜率
#4.

import sys
import time
sys.path.append('..')
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from spider_stock.StockHelper import StockHelper
from spider_stock.help import  *

from mysql.proxy_api import proxy_list
import socket
import random
#构建2个代理ip
from datetime import datetime

stock_helper = StockHelper()

day_date = datetime.now().strftime("%Y-%m-%d")


while True:
    one = stock_helper.random_stock()
    sid = one[1]
    link = 'http://d.10jqka.com.cn/v6/time/hs_%s/last.js'%(sid)
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js'%(sid)
    referer = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
    key = 'hs_%s'%(sid)
    price_min = 9999999
    price_max = -9999999
    money_min = 9999999
    money_max = -99999999
    #主要获取股票价格，是否涨停
    content = stock_helper.getStockPrciePoints(link)

    if content is None:
        time.sleep(random.uniform(62, 65))
        continue
    arr = content.split('last(')

    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)

    all = json_content[key]
    pre = float(all['pre'])  # 昨收
    price_data_arr = all['data'].split(';')
    name = all['name']
    temp_price = []
    for one_point in price_data_arr:
        info = one_point.split(',')
        one_price = float(info[1])
        if one_price < price_min:
            price_min = one_price
        if one_price > price_max:
            price_max = one_price
        temp_price.append(one_price)
    price = []
    for one in temp_price:
        price.append(round(realPoint(price_min,price_max,one),2))

    #获取money
    content = stock_helper.getStockMoneyPoints(money_link)

    if content is None:
        time.sleep(random.uniform(121, 123))
        continue
    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)
    all = json_content[key]
    money_data_arr = all['data'].split(';')
    temp_money = []
    for one_point in money_data_arr:
        money_info = one_point.split(',')

        p1 = float(money_info[1])
        p2 = float(money_info[2])
        p3 = float(money_info[3])
        p4 = float(money_info[4])
        p5 = float(money_info[5])
        p6 = float(money_info[6])
        p7 = float(money_info[7])
        p8 = float(money_info[8])
        big_money = round( (p1-p2+p3-p4)/10000,1)
        if big_money < money_min:
            money_min = big_money
        if big_money > money_max:
            money_max = big_money
        temp_money.append(big_money)
    money = []
    for one in temp_money:
        money.append(round(realPoint(money_min,money_max,one),2))
    #构造x轴
    x_num = min(len(price),len(money))
    x = list(range(x_num))
    #斜率
    price_slope = all_half_slope(x,price)
    money_slope = all_half_slope(x,money)
    #开始分析，满足条件存记录,就存日期和all_k,的所有点，和all_k,half_k
    if True:
        price_all_slope = price_slope[0]
        price_half_slope = price_slope[1]
        money_all_slope = money_slope[0]
        moeny_half_slope = money_slope[1]
        price_slope_content = json.dumps(price)
        money_slope_content = json.dumps(money)
        sql = "insert into tan_second values (null,'%s','%s',%s,%s,%s,%s,'%s','%s')"%\
              (sid,day_date,price_all_slope,price_half_slope,money_all_slope,moeny_half_slope,price_slope_content,money_slope_content)

        stock_helper.insertStockRecord(sql)
    #两分钟抓一只
    time.sleep(random.uniform(121, 123))
    exit()