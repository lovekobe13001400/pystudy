import urllib.request
class Help():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc',
            'Referer':'http://stockpage.10jqka.com.cn/HQ_v4.html'
        }
    #获取新浪股票信息
    def sina_stock(self,gid='sz002415'):
        url = "http://hq.sinajs.cn/list=%s"%gid
        response = urllib.request.urlopen(url)
        content = response.read().decode('gbk')
        info_arr = content.split(',')
        price_now = info_arr[3]
        return price_now

    def getStockMoneyPoints(self, link, handler_obj={}):
        # today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

money_url = 'http://d.10jqka.com.cn/v2/moneyflow/hs_002415/last.js'
h = Help()
print(h.getStockMoneyPoints(money_url))
