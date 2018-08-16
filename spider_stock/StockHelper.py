import time
import random
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
            # 'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc',
            # 'Referer':'http://stockpage.10jqka.com.cn/HQ_v4.html'
        }

        self.user_agent_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

    def getStockPrciePoints(self,link,handler_obj={}):
        time_now = int(time.time())

        cookie = "spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1="+str(time_now)+"; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc"
        self.headers['Cookie'] = cookie
        # ua = random.choice(self.user_agent_list)
        # if ua:
        #     self.headers["User-Agent"] = ua
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
    def getStockPrciePoints1(self,link,handler_obj={}):
        time_now = int(time.time())

        #cookie = "spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1="+str(time_now)+"; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc"
        self.headers['Cookie'] = 'searchGuide=sg; spversion=20130314; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1533263275,1533432205,1533469822,1533472700; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1533472700; historystock=002815%7C*%7C002415%7C*%7C002563%7C*%7C600130%7C*%7C000801; v=AiUE6KiNkkJ8fvYeZV9tagXINOpcYtmcIxa9SicK4dxrPksc77LpxLNmzQW0'
        self.headers['Referer'] = 'http://stockpage.10jqka.com.cn/realHead_v2.html'
        self.headers['Host'] = 'd.10jqka.com.cn'
        # ua = random.choice(self.user_agent_list)
        # if ua:
        #     self.headers["User-Agent"] = ua
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
    def getStockPrciePoints2(self,link,handler_obj={}):
        time_now = int(time.time())

        #cookie = "spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1="+str(time_now)+"; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc"
        self.headers['Cookie'] = 'searchGuide=sg; spversion=20130314; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1533263275,1533432205,1533469822,1533472700; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1533472700; historystock=002815%7C*%7C002415%7C*%7C002563%7C*%7C600130%7C*%7C000801; v=Au3MQLBlSir0li5GbUqlUr1w_IJkSiM1q3-Fty_yLUzyYwP095ox7DvOlaW8'
        self.headers['Referer'] = 'http://stockpage.10jqka.com.cn/002815/'
        # ua = random.choice(self.user_agent_list)
        # if ua:
        #     self.headers["User-Agent"] = ua
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
    def getStockPrciePoints3(self,link,handler_obj={}):
        time_now = int(time.time())

        #cookie = "spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1="+str(time_now)+"; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc"
        self.headers['Cookie'] = 'searchGuide=sg; spversion=20130314; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1533263275,1533432205,1533469822,1533472700; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1533472700; historystock=002815%7C*%7C002415%7C*%7C002563%7C*%7C600130%7C*%7C000801; v=AkdmUmbj0LiK6FQ0-mBvYDOe1vASTB_MdSGftRk0Y8P9Q2nmIRyrfoXwL-Mq'
        self.headers['Referer'] = 'http://stockpage.10jqka.com.cn/HQ_v4.html'
        self.headers['Host'] = 'd.10jqka.com.cn'
        # ua = random.choice(self.user_agent_list)
        # if ua:
        #     self.headers["User-Agent"] = ua
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
        ua = random.choice(self.user_agent_list)
        if ua:
            self.headers["User-Agent"] = ua
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
