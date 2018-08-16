#coding=utf-8
import urllib.request
import json
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
from lxml import etree
from func import is_float
import time
#构建2个代理ip
httpproxy_handler = urllib.request.ProxyHandler({"http" : "117.90.3.190:9000"})
nullproxy_handler = urllib.request.ProxyHandler({})
helper = MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
#定义一个代理开关
proySwitch = False

if(proySwitch):
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; refreshStat=off; user=MDp3YWtlcmN5OjpOb25lOjUwMDozNzU4ODE2MTg6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjI1Ojo6MzY1ODgxNjE4OjE1MjkyNDE5MzI6OjoxNDgwNTk0ODYwOjMxNTI2ODowOjEzYmMxYTU3ZTQ5MjRmZDdhNGYzNGZlYzY4OTNjMjE5MzpkZWZhdWx0XzI6MA%3D%3D; userid=365881618; u_name=wakercy; escapename=wakercy; ticket=30158138cccbcb9c7c8fa673af7ce4ce; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1528942207,1529030502,1529232862,1529287863; Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1528942207,1529030502,1529232862,1529287863; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528942207,1529030502,1529232862,1529287863; historystock=300666%7C*%7C600121%7C*%7C300345%7C*%7C600546%7C*%7C300139; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1529299647; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1529299647; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1529302328; searchGuide=sg; v=AruatnLfZOXyJlhR0Fz0uI3lSpQgEMd2yTySya14ldPTCNVANeBfYtn0Iw6-'
}
all_plate_sql = "select * from tan_plate"
all_paltes = helper.get_all(all_plate_sql)
# print(all_paltes)
# params = {'name': '阿里巴巴概念', 'sid': 'aa', 'price': 1109.905, 'time_point': 930.0, 'date': '2018-06-14', 'zdf': -0.54, 'pre': 1115.926, 'volume': 5475532}
# print(params)
# sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
# helper.insert(sql,params)

page = 3
while(1):
    page+=1
    if(page>=72):
        break
    link = 'http://data.10jqka.com.cn/ajax/yjgg/date/2018-03-31/board/ALL/field/DECLAREDATE/page/%s/ajax/1/'%(page)
    referer = 'http://data.10jqka.com.cn/financial/yjgg/'
    temp_hedaers = headers
    temp_hedaers['Referer'] = referer
    request = urllib.request.Request(link, headers=temp_hedaers)
    response = opener.open(request)
    html = response.read()

    html =  html.decode('gbk')
    selector = etree.HTML(html)
    item = {}
    for sel in selector.xpath('//table/tbody/tr'):
        item['sid'] = str(sel.xpath('td[2]/a/text()')[0])
        item['sname'] = str(sel.xpath('td[3]/a/text()')[0])
        item['time_date'] = str(sel.xpath('td[4]/text()')[0])
        item['yy_tb'] = str(sel.xpath('td[6]/text()')[0])
        item['yy_hb'] = str(sel.xpath('td[7]/text()')[0])
        item['lr_tb'] = str(sel.xpath('td[9]/text()')[0])
        item['lr_hb'] = str(sel.xpath('td[10]/text()')[0])
        if(is_float(item['yy_tb'])):
            pass
        else:
            item['yy_tb'] = 0

        if (is_float(item['yy_hb'])):
            pass
        else:
            item['yy_hb'] = 0

        if (is_float(item['lr_tb'])):
            pass
        else:
            item['lr_tb'] = 0
        if (is_float(item['lr_hb'])):
            pass
        else:
            item['lr_hb'] = 0

        sql = 'insert into tan_report values(null,%(sid)s,%(sname)s,%(time_date)s,%(yy_tb)s,%(yy_hb)s,%(lr_tb)s,%(lr_hb)s)'
        helper.insert(sql,item)
    time.sleep(65)
    # for one_point in data_arr:
    #     info = one_point.split(',')
    #     time_point = int(info[0])
    #     price = float(info[1])
    #     zdf = round((price-pre)/pre*100,2)
    #     volume = int(info[4])
    #     params = {"name": name, "sid": sid, "price": price,"time_point":time_point, "date": today,"zdf":zdf,"pre":pre,"volume":volume}
    #     sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
    #     print(params)
    #     helper.insert(sql,params)
        #print(helper)




