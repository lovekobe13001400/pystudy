# middlewares.py

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import base64



# 随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        USER_AGENTS = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
        ]
        useragent = random.choice(USER_AGENTS)

        request.headers.setdefault("User-Agent", useragent)

class RandomProxy(object):
    def process_request(self, request, spider):
        PROXIES = ['101.37.79.125:3128']

        proxy = random.choice(PROXIES)
        print(proxy)
        # # 对账户密码进行base64编码转换
        # base64_userpasswd = base64.b64encode(proxy['user_passwd'])
        # # 对应到代理服务器的信令格式里
        # request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
        request.meta['proxy'] = "http://" + proxy
