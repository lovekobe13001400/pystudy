#爬取有用的ip
#coding=utf-8
'''
获取每天版块的数据
'''
import sys
sys.path.append('..')
import urllib.request
import json
import threading
from mysql.MysqlHelper import MysqlHelper
from datetime import datetime
from mysql.proxy_api import proxy_list
import time
from spider_stock_old.StockHelper import StockHelper
stock_helper = StockHelper()
helper = MysqlHelper()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
}

lock = threading.Lock()
def getIp():
    link = "http://www.tan66.com/"
    while True:
        ip, port, scheme = stock_helper.randomIp()
        handler_obj = {}
        handler_obj[scheme] = ip + ':' + port
        content = stock_helper.getStockMoneyPoints(link, handler_obj)
        if content is None:
            lock.acquire()
            stock_helper.updateIp(ip, port, scheme, 0)
            lock.release()
        else:
            lock.acquire()
            stock_helper.updateIp(ip, port, scheme, 1)
            lock.release()



for i in range(50):
    t1 = threading.Thread(target=getIp)
    t1.start()
