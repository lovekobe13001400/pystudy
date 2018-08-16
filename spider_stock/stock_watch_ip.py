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
ip_sql = "select * from ip where success_num>0 order by success_num desc limit 30"
ip_list = helper.get_all(ip_sql)
all_ip_num = len(ip_list)
ip_num = 0
for one in all_report:
    #获取60个可用ip
    sid = one[1]
    link = 'http://d.10jqka.com.cn/v6/time/hs_%s/last.js'%(sid)
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js'%(sid)
    referer = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
    key = 'hs_%s'%(sid)
    #
    while(ip_num<all_ip_num):
        ip_arr = ip_list[ip_num]
        handler_obj = {}
        handler_obj[ip_arr[3]] = ip_arr[1]+':'+ip_arr[2]
        update_sql = 'update ip set last_time=%s where ip="%s"'% (now_time,ip_arr[1])
        helper.update(update_sql)
        try:
            ip_num += 1
            request = urllib.request.Request(link, headers=headers)
            httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
            opener = urllib.request.build_opener(httpproxy_handler)
            response = opener.open(request)
            break
        except Exception as e:
            print(e)
            ip_num += 1
            if(ip_num>=all_ip_num):
                #重新获取ip池
                ip_sql = "select * from ip where last_time>%s order by success_num desc limit 30"%(dif_now_time)
                ip_list = helper.get_all(ip_sql)
                all_ip_num = len(ip_list)
                ip_num = 0
            continue
    content = response.read().decode()
    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)

    all = json_content[key]
    pre = float(all['pre'])#昨收

    data_arr = all['data'].split(';')
    name = all['name']
    ##大中小单处理
    while(ip_num<all_ip_num):
        ip_arr = ip_list[ip_num]
        handler_obj = {}
        handler_obj[ip_arr[3]] = ip_arr[1] +':'+ ip_arr[2]
        update_sql = 'update ip set last_time=%s where ip="%s"'%(now_time,ip_arr[1])
        helper.update(update_sql)
        try:
            ip_num += 1
            request = urllib.request.Request(money_link, headers=headers)
            httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
            opener = urllib.request.build_opener(httpproxy_handler)
            response = opener.open(request)
            break
        except Exception as e:
            print(e)
            ip_num += 1
            if (ip_num >= all_ip_num):
                # 重新获取ip池
                ip_sql = "select * from ip where last_time>%s order by success_num desc limit 30" % (dif_now_time)
                ip_list = helper.get_all(ip_sql)
                all_ip_num = len(ip_list)
                ip_num = 0
            continue
    content = response.read().decode()
    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)
    all = json_content[key]
    money_data_arr = all['data'].split(';')

    #处理两组数据
    k = 0
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
        params = {"name": name, "sid": sid, "price": price, "time_point": time_point, "date": today, "zdf": zdf, "pre": pre,"volume": volume,
                  "p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,"p7":p7,"p8":p8}
        sql = 'insert into tan_stock_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s,' \
              '%(p1)s,%(p2)s,%(p3)s,%(p4)s,%(p5)s,%(p6)s,%(p7)s,%(p8)s)'

        helper.insert(sql,params)
        #就插一条
        break
