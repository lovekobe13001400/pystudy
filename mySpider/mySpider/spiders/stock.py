# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import StockItem

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/gn/']
    def parse(self, response):
        for sel in response.xpath('//div[contains(@class,"cate_items")]/a'):
            item = StockItem()
            link = sel.xpath('@href').extract()[0]
            link_arr = link.split('/')
            item['url_code'] = link_arr[len(link_arr)-2]
            yield scrapy.Request(link, meta={'item':item},callback=self.parse2)
            #二级页面爬取
    def parse2(self,response):
        item = response.meta['item']
        item['sid'] = response.xpath('//div[contains(@class,"board-hq")]/h3/span/text()').extract()[0]
        item['gn_name'] = response.xpath('//div[contains(@class,"board-hq")]/h3/text()').extract()[0]
        return item
