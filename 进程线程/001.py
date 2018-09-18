import sys
sys.path.append('..')
import time,threading
import urllib.request
import json
from spider_stock.StockHelper import StockHelper
def getMoney(n):
    while True:
        print(n)
        time.sleep(1)
stock_helper = StockHelper()
def randomIp():
    res = urllib.request.urlopen('http://47.75.51.71:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous')
    #res = urllib.request.urlopen('http://127.0.0.1:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous')
    html = res.read().decode()
    json_content = json.loads(html)
    ip = json_content['data']['detail'][0]['ip']
    scheme = json_content['data']['detail'][0]['scheme']
    port = json_content['data']['detail'][0]['port']
    return ip,port,scheme
def ipList():
    res = urllib.request.urlopen('http://47.75.51.71:12345/api/proxy/?count=5&scheme=HTTP&anonymity=anonymous')
    # res = urllib.request.urlopen('http://127.0.0.1:12345/api/proxy/?count=1&scheme=HTTP&anonymity=anonymous')
    html = res.read().decode()
    json_content = json.loads(html)
    iplist = json_content['data']['detail']
    handler_obj_list = []
    for one in iplist:
        ip = one['ip']
        scheme = one['scheme']
        port = one['port']
        handler_obj_list.append((ip,port,scheme))
    return handler_obj_list
def getContent():
    ip,port,scheme = randomIp()
    handler_obj= {}
    handler_obj[scheme] = ip+':'+port

    while True:
        money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_002415/last.js'
        content = stock_helper.getStockMoneyPoints(money_link,handler_obj=handler_obj)
        global n
        if content is None:
            ip, port, scheme = randomIp()
            handler_obj = {}
            handler_obj[scheme] = ip + ':' + port
            # n += 1
            # print(n)
            continue
        else:
            n += 1
            print(n)
n = 0
for i in range(50):
    t1 = threading.Thread(target=getContent)
    t1.start()

