import configparser
import os
import sys
import json
cf = configparser.ConfigParser()
test = cf.read(sys.path[0]+'/inv')

def getConfig():
    conf = {}
    conf['local_ip'] = cf.get('env','local_ip')
    conf['proxy_ip'] = cf.get('env','proxy_ip')
    return conf


def decode_stock_json(content):

    c1 = content.split('last(')[1].strip(')')
    c2 = json.loads(c1)
    return c2

#给定price_content和money_content，判断是否需要观察
def should_watch(sid,price_content,money_content):
    key = 'hs_%s' % (sid)
    price_dict = decode_stock_json(price_content)
    money_dict = decode_stock_json(money_content)

    price_data = price_dict[key]['data'].split(';')
    #昨日封盘价
    pre = float(price_dict[key]['pre'])
    money_data = money_dict[key]['data'].split(';')
    # price所有价格集合，所有money集合
    price = []
    money = []
    x = []
    xi = 0
    price_min = 9999999
    price_max = -9999999
    money_min = 9999999
    money_max = -99999999
    price_all_half_slope = (0, 0)
    money_all_half_slope = (0, 0)
    # 只为了得出最大值和最小值

    for i in range(len(price_data)):
        xi += 1
        x.append(xi)
        price_temp_arr = price_data[i].split(',')
        temp_price = float(price_temp_arr[1])
        money_temp_arr = money_data[i].split(',')
        temp_money = (float(money_temp_arr[1]) - float(money_temp_arr[2]) + float(money_temp_arr[3]) - float(
            money_temp_arr[4])) / 1000

        if temp_price > price_max:
            price_max = temp_price
        if temp_price < price_min:
            price_min = temp_price
        if temp_money > money_max:
            money_max = temp_money
        if temp_money < money_min:
            money_min = temp_money

    pzdf_min = round((price_min - pre) / pre * 100, 1)
    pzdf_max = round((price_max - pre) / pre * 100, 1)
    #取price_data和money_data的最小长度，
    for i in range(len(price_data)):
        # 第i个点
        # 股价
        price_temp_arr = price_data[i].split(',')
        temp_price = float(price_temp_arr[1])

        # 大单
        money_temp_arr = money_data[i].split(',')
        temp_money = (float(money_temp_arr[1]) - float(money_temp_arr[2]) + float(money_temp_arr[3]) - float(
            money_temp_arr[4])) / 1000

        price.append(realPoint(price_min, price_max, temp_price))
        money.append(realPoint(money_min, money_max, temp_money))

    money_all_half_slope = all_half_slope(x, money)
    price_all_half_slope = all_half_slope(x, price)
    return money_all_half_slope,price_all_half_slope