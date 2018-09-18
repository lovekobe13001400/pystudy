import time
import sys
sys.path.append('..')
from datetime import datetime
import urllib.request
from mysql.MysqlHelper import *
class StockHelper():
    #获取股票的时间点-价格
    def __init__(self):
        self.mysql_helper = MysqlHelper()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc',
            'Referer':'http://stockpage.10jqka.com.cn/HQ_v4.html'
        }
    def getStockPrciePoints(self,link,handler_obj={}):
        try:
            request = urllib.request.Request(link, headers=self.headers)
            httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
            #socket.setdefaulttimeout(10)
            opener = urllib.request.build_opener(httpproxy_handler)
            response = opener.open(request)
            content = response.read().decode()
            return content
        except Exception as e:
            print(e)
            return None


    #获取股票的时间-大中小单
    def getStockMoneyPoints(self,link,handler_obj={}):
        #today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            request = urllib.request.Request(link, headers=self.headers)
            httpproxy_handler = urllib.request.ProxyHandler(handler_obj)
            opener = urllib.request.build_opener(httpproxy_handler)
            response = opener.open(request)
            content = response.read().decode()
            return content
        except Exception as e:
            print(e)
            return None
    #获取可用ip
    def getUsefulIp(self):
        now_time = int(time.time())
        dif_now_time = int(time.time()) - 80
        ip_sql = "select * from ip where last_time<%s order by success_num desc limit 30" % (dif_now_time)
        ip_list = self.mysql_helper.get_all(ip_sql)
        return ip_list
    #更新ip使用过
    def updateIpUse(self,ip):
        now_time = int(time.time())
        update_sql = 'update ip set last_time=%s where ip="%s"' % (now_time, ip)
        return self.mysql_helper.update(update_sql)

    #
    def getWatchStock(self):
        sql = "select * from tan_stock where is_watch=1"
        list = self.mysql_helper.get_all(sql)
        return list;

    def insertStockRecord(self,sql):
        return self.mysql_helper.insert(sql)

