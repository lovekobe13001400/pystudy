# -*- coding: utf-8 -*-
import scrapy


class ProxyCheckSpider(scrapy.Spider):
    name = 'proxy_check'
    allowed_domains = ['p.com']
    start_urls = ['http://p.com/']

    def parse(self, response):
        pass
