# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import StockPointItem
class StockPointSpider(scrapy.Spider):
    name = 'stock_point'
    allowed_domains = ['10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/gn/']

    def parse(self, response):
        item = StockPointItem()
        js_url = 'http://d.10jqka.com.cn/v4/time/bk_885312/last.js'
        scrapy.Request(js_url,callback=self.parse2)
        #print(type(c))
        # file = open('stock.json', 'wb')
        # file.write(c)

        # print('aaaaaaaaaaaaa')
        # item['name'] = c
        # for sel in response.xpath('//div[contains(@class,"cate_items")]/a'):
        #     link = sel.xpath('@href').extract()[0]
        #     link = 'http://d.10jqka.com.cn/v4/time/bk_885751/last.js'
        #     yield scrapy.Request(link, callback=self.parse2)
        #     break

            # 二级页面爬取

    def parse2(self, response):
        item = StockPointItem()
        #sid = response.xpath('//div[contains(@class,"board-hq")]/h3/span/text()').extract()[0]
        print('aaaaaaaaaaaaa')
        print('bbbbbbbbbbbbb')
        print(response)
        # refer_url = response.request.url
        # js_url = 'http://d.10jqka.com.cn/v4/time/bk_$s/last.js'(sid)
        #scrapy.Request(js_url)
        # item['gn_name'] = response.xpath('//div[contains(@class,"board-hq")]/h3/text()').extract()[0]
        # item['zdf'] = response.xpath('//div[contains(@class,"board-infos")]/dl/dd/text()').extract()[5]
        # item['zdf'] = item['zdf'].split('%')[0]
        # item['zdf'] = float(item['zdf'])
        return item

    def parse3(self,reponse):
        pass