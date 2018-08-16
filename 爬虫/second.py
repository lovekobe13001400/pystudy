#coding=utf-8
'''
实时获取
'''
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from mysql.juhe import juhe
from datetime import datetime
from mysql.proxy_api import proxy_list
from lxml import etree
import time
import socket
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
#获取海康威视相关的
sid_arr = [ '885378','885745','885790','885423','885312','885362','885728','885452']
sid_str = '885378,885745,885790,885423,885312,885362,885728,885452'
all_plate_sql = "select * from tan_plate where sid in (%s)"%(sid_str)
all_paltes = helper.get_all(all_plate_sql)

point_num = 0
today = datetime.now().strftime('%Y-%m-%d')
last = {}
last['885378'] = 0
last['885745'] = 0
last['885790'] = 0
last['885423'] = 0
last['885312'] = 0
last['885362'] = 0
last['885728'] = 0
last['885452'] = 0

while(1):
    for one_plate in all_paltes:
        #获取每个概念版块的涨幅，
        url = 'http://q.10jqka.com.cn/gn/detail/code/%s/'%(one_plate[3])
        name = one_plate[2]
        sid =  one_plate[1]
        #构造请求头
        referer = 'http://q.10jqka.com.cn/gn/'
        temp_hedaers = headers
        temp_hedaers['Referer'] = referer
        request = urllib.request.Request(url,headers=temp_hedaers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('gbk')
        selector = etree.HTML(content)
        try:
            zdf = str(selector.xpath('//div[contains(@class,"board-infos")]/dl[6]/dd/text()')[0])
            new_zdf = zdf.strip('%')
        except Exception as e:
            new_zdf = last[sid]
            print(name)
            print(e)

        last[sid] = new_zdf
        #zdf = selector.xpath('//.board-infos/dl[6]/dd/text()')
        params = {"name": name, "sid": sid, "time_point": point_num, "date": today, "zdf": new_zdf}
        sql = 'insert into tan_second_record values(null,%(name)s,%(sid)s,%(time_point)s,%(date)s,%(zdf)s)'
        helper.insert(sql, params)

    #海康威视股票
    stock_info = juhe('sz002415')
    zdf = stock_info['increPer']
    params = {"name": '海康威视', "sid": '002415', "time_point": point_num, "date": today, "zdf": zdf}
    sql = 'insert into tan_second_record values(null,%(name)s,%(sid)s,%(time_point)s,%(date)s,%(zdf)s)'
    helper.insert(sql, params)
    #每30s更新一次数据
    point_num += 1
    time.sleep(60)

