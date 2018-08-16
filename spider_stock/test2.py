
#coding=utf-8
'''
获取每天个股的数据(部分股票)
'''
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
import time
import socket
from mysql.proxy_api import proxy_list
#构建2个代理ip
httpproxy_handler = urllib.request.ProxyHandler({"http" : "117.163.55.23:8123"})
nullproxy_handler = urllib.request.ProxyHandler({})
helper = MysqlHelper()
#请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc',
    'Referer':'http://stockpage.10jqka.com.cn/HQ_v4.html'
}
today = datetime.now().strftime('%Y-%m-%d')
proxy_url = 'http://47.75.51.71:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'
sql = "select * from tan_stock"
all_stock = helper.get_all(sql)
for one in all_stock:
    sid = one[2]
    sname = one[3]
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js'%(sid)
    key = 'hs_%s'%(sid)
    while(1):
        proxy_request = urllib.request.Request(proxy_url)
        proxy_response = urllib.request.urlopen(proxy_request)
        proxy_content = proxy_response.read().decode('utf-8')
        json_content = json.loads(proxy_content)
        ip = json_content['data']['detail'][0]['ip']
        port = json_content['data']['detail'][0]['port']
        scheme = json_content['data']['detail'][0]['scheme']
        handler_obj = {}
        handler_obj[scheme] = ip+':'+port

        try:
            httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
            socket.setdefaulttimeout(3)
            opener = urllib.request.build_opener(httpproxy_handler)
            request = urllib.request.Request(money_link, headers=headers)
            response = opener.open(request)
            content = response.read().decode()
            # 成功说明代理没问题
            break
        except Exception as e:
            # 不停换代理直到成功为止
            print(e)

    arr = content.split('last(')
    json_content = arr[1].strip(')')
    json_content = json.loads(json_content)
    all = json_content[key]
    money_data_arr = all['data'].split(';')
    #处理两组数据
    k = 0
    for one_point in money_data_arr:
        info = one_point.split(',')
        time_point = int(info[0])
        price = float(info[1])
        # 这些数据暂时不要
        zdf = 0
        pre = 0
        volume = 0
        date = today
        p1 = info[1]
        p2 = info[2]
        p3 = info[3]
        p4 = info[4]
        p5 = info[5]
        p6 = info[6]
        p7 = info[7]
        p8 = info[8]
        params = {"name": sname, "sid": sid, "price": price, "time_point": time_point, "date": today, "zdf": zdf, "pre": pre,"volume": volume,
                  "p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,"p7":p7,"p8":p8}
        sql = 'insert into tan_stock_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s,' \
              '%(p1)s,%(p2)s,%(p3)s,%(p4)s,%(p5)s,%(p6)s,%(p7)s,%(p8)s)'
        helper.insert(sql,params)





# #coding=utf-8
# '''
# 获取每天版块的数据
# '''
# import urllib.request
# import json
# from mysql.MysqlHelper import MysqlHelper
# from datetime import datetime
# from mysql.proxy_api import proxy_list
# import time
# import socket
# import redis
# #连接redis服务器
# redis_res = redis.StrictRedis(host='localhost',port=6379,password='',db=1)
#
# #构建2个代理ip
# httpproxy_handler = urllib.request.ProxyHandler({"http" : "117.90.3.190:9000"})
# nullproxy_handler = urllib.request.ProxyHandler({})
# helper = MysqlHelper()
# #定义一个代理开关
# proySwitch = False
#
# if(proySwitch):
#     opener = urllib.request.build_opener(httpproxy_handler)
# else:
#     opener = urllib.request.build_opener(nullproxy_handler)
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
#     'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
# }
# #获取海康威视相关的
# sid_arr = [ '885378','885745','885790','885423','885312','885362','885728','885452']
# sid_str = '885378,885745,885790,885423,885312,885362,885728,885452'
# #all_plate_sql = "select * from tan_plate where sid in (%s)"%(sid_str)
# all_stock_sql = "select * from tan_stock"
# all_stock= helper.get_all(all_stock_sql)
# #遍历概念版块
# p_list = {}
# proxy_url = 'http://47.75.51.71:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'
# referer = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
# headers['Referer'] = referer
# for one in all_stock:
#     sid = one[2]
#     money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js' % (sid)
#     # 使用代理
#     while(1):
#         proxy_request = urllib.request.Request(proxy_url)
#         proxy_response = urllib.request.urlopen(proxy_request)
#         proxy_content = proxy_response.read().decode('utf-8')
#         json_content = json.loads(proxy_content)
#         ip = json_content['data']['detail'][0]['ip']
#         port = json_content['data']['detail'][0]['port']
#         scheme = json_content['data']['detail'][0]['scheme']
#
#         handler_obj = {}
#         handler_obj[scheme] = ip+':'+port
#         try:
#             httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
#             socket.setdefaulttimeout(3)
#             opener = urllib.request.build_opener(httpproxy_handler)
#             request = urllib.request.Request(money_link, headers=headers)
#             response = opener.open(request)
#             # 成功说明代理没问题
#             break
#         except Exception as e:
#             # 不停换代理直到成功为止
#             print(e)
#     response = opener.open(request)
#     content = response.read().decode()
#     arr = content.split('last(')
#     json_content = arr[1].strip(')')
#     json_content = json.loads(json_content)
#     all = json_content[key]
#     money_data_arr = all['data'].split(';')
#
#     # 处理两组数据
#     k = 0
#     for one_point in data_arr:
#         info = one_point.split(',')
#         print(info)
#         time_point = int(info[0])
#         price = float(info[1])
#         zdf = round((price - pre) / pre * 100, 2)
#         volume = int(info[4])
#         price = price
#         volume = volume
#         time_point = time_point
#         date = today
#         money_info = money_data_arr[k].split(',')
#         p1 = money_info[1]
#         p2 = money_info[2]
#         p3 = money_info[3]
#         p4 = money_info[4]
#         p5 = money_info[5]
#         p6 = money_info[6]
#         p7 = money_info[7]
#         p8 = money_info[8]
#         params = {"name": name, "sid": sid, "price": price, "time_point": time_point, "date": today, "zdf": zdf,
#                   "pre": pre, "volume": volume,
#                   "p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5, "p6": p6, "p7": p7, "p8": p8}
#         sql = 'insert into tan_stock_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s,' \
#               '%(p1)s,%(p2)s,%(p3)s,%(p4)s,%(p5)s,%(p6)s,%(p7)s,%(p8)s)'
#
#         helper.insert(sql, params)
#         k += 1
#     # try:
#     #     content = response.read().decode()
#     #     arr = content.split('last(')
#     #     json_content = arr[1].strip(')')
#     #     json_content = json.loads(json_content)
#     #     key = 'bk_%s' % (one[1])
#     #     all = json_content[key]
#     #     pre = float(all['pre'])  # 昨收
#     #     data_arr = all['data'].split(';')
#     #     name = all['name']
#     #     sid = one[1]
#     #     today = datetime.now().strftime('%Y-%m-%d')
#     #     for one_point in data_arr:
#     #         info = one_point.split(',')
#     #         time_point = int(info[0])
#     #         price = float(info[1])
#     #         zdf = round((price - pre) / pre * 100, 2)
#     #         volume = int(info[4])
#     #         params = {"name": name, "sid": sid, "price": price, "time_point": time_point, "date": today, "zdf": zdf,
#     #                   "pre": pre, "volume": volume}
#     #         sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
#     #         helper.insert(sql, params)
#     # except Exception as e:
#     #     print(e)



