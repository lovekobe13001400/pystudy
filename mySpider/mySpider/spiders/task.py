# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import MyspiderItem
class TaskSpider(scrapy.Spider):
    name = 'task'
    allowed_domains = ['sjq.cn']
    start_urls = ['http://sjq.cn/']

    def parse(self, response):
        # print(response.xpath('//ul/li'))zz
        for sel in response.xpath('//ul[contains(@class,"hot-product")]/li'):
            item = MyspiderItem()
            item['img'] = sel.xpath('a/div[contains(@class,"h-img")]/img/@src').extract()
            item['name'] = sel.xpath('a/div[contains(@class,"h-name")]/text()').extract()
            item['price'] = sel.xpath('a/div[contains(@class,"h-price")]/text()').extract()
            yield item