#from urllib import request
#你好
import sys
sys.path.append('..')
import urllib.request
import json
from spider_stock.StockHelper import StockHelper
stock_helper = StockHelper()

# ip,port,scheme = stock_helper.randomIp()
# handler_obj= {}
# handler_obj[scheme] = ip+':'+port

n = 0
# while True:
#     money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_002415/last.js'
#     content = stock_helper.getStockMoneyPoints(money_link,handler_obj=handler_obj)
#     if content is None:
#         ip, port, scheme = stock_helper.randomIp('47.75.51.71')
#         handler_obj = {}
#         handler_obj[scheme] = ip + ':' + port
#         continue
#     else:
#         n += 1
#     print(n)
handler_obj_list = stock_helper.randomIpFromDb()
for handler_obj in handler_obj_list:
    money_link = 'http://d.10jqka.com.cn/v2/moneyflow/hs_002415/last.js'
    content = stock_helper.getStockMoneyPoints(money_link,handler_obj=handler_obj)
    if content:
        n+=1
        print(n)
    else:
        print('fail')
    # if content is None:
    #     ip, port, scheme = stock_helper.randomIpFromDb()
    #     handler_obj = {}
    #     handler_obj[scheme] = ip + ':' + port
    #     print('fail')
    #     continue
    # else:
    #     n += 1




