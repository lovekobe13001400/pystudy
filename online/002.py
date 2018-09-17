# !/usr/bin/env python
#coding=utf-8
import sys
import threading,time
import datetime
import urllib.request
import json
sys.path.append('..')
from online import help
from online.StockHelper import StockHelper
conf = help.getConfig()
stock_helper = StockHelper()
today = datetime.datetime.now().strftime('%Y-%m-%d')

def randomIp():

    res = urllib.request.urlopen('http://%s/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'%(conf['proxy_ip']))
    url = 'http://%s/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous'%(conf['proxy_ip'])

    html = res.read().decode()

    json_content = json.loads(html)

    ip = json_content['data']['detail'][0]['ip']

    scheme = json_content['data']['detail'][0]['scheme']

    port = json_content['data']['detail'][0]['port']

    return ip,port,scheme

def getContent(threa_no):
    #进程编号threa_no
    ip,port,scheme = randomIp()
    handler_obj= {}
    handler_obj[scheme] = ip+':'+port
    #获取属于这个线程应该操作的股票
    offset = threa_no*4

    mylock.acquire()
    threa_stock_list = stock_helper.getWatchStock(offset)
    mylock.release()
    for i in range(len(threa_stock_list)):
        #不停的用ip去请求，直到成功获取，才开始下一个股票
        is_success = 0
        sid = threa_stock_list[i][1]
        while True:
            price_link = 'http://d.10jqka.com.cn/v6/time/hs_%s/last.js'%(sid)
            price_content = stock_helper.getStockMoneyPoints(price_link,handler_obj=handler_obj)


            money_content = ""
            #正常获取
            if price_content:
                if '<html>' in price_content:
                    ip, port, scheme = randomIp()
                    handler_obj = {}
                    handler_obj[scheme] = ip + ':' + port
                    continue
                #入库
                sql = "insert into tan_stock_content VALUES (null,'%s','%s','%s','%s')"%(sid,price_content,money_content,today)
                #加锁
                mylock.acquire()
                content_id = stock_helper.insertStockRecord(sql)
                mylock.release()
                is_success = 1
                break
            else:
                ip, port, scheme = randomIp()
                handler_obj = {}
                handler_obj[scheme] = ip + ':' + port
                continue
        if is_success:
            #price获取成功再获取money
            while True:
                money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_%s/last.js' % (sid)
                money_content = stock_helper.getStockMoneyPoints(money_link,handler_obj=handler_obj)
                # 正常获取
                if money_content:
                    if '<html>' in money_content:
                        ip, port, scheme = randomIp()
                        handler_obj = {}
                        handler_obj[scheme] = ip + ':' + port
                        continue
                    # 入库
                    sql = "UPDATE tan_stock_content set money_content='%s' where id=%s" % (money_content,content_id)
                    # 加锁
                    mylock.acquire()
                    stock_helper.updateStock(sql)
                    mylock.release()
                    break
                else:
                    ip, port, scheme = randomIp()
                    handler_obj = {}
                    handler_obj[scheme] = ip + ':' + port
                    continue
    print('threa_no:%s finish'%(threa_no))

mylock = threading.Lock()
for i in range(20):
    t1 = threading.Thread(target=getContent,args=(i,))
    t1.start()
