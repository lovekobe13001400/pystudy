# -*- coding: utf-8 -*-
import random,base64

class ProxyMiddleware(object):
    proxyList = [
        '183.167.217.152:6300', '114.226.105.154:6666',
    ]
    def process_request(self,request,spider):
        pro_adr = random.choice(self.proxyList)
        request.meta['proxy'] = "http://"+pro_adr
