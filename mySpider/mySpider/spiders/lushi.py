# -*- coding: utf-8 -*-
'''
爬取所有炉石数据库卡牌的数据，存储并且保存图片
网址链接：http://db.duowan.com/lushi
生成爬虫：scrapy genspider tencent "tencent.com"
运行爬虫：scrapy crawl lushi
'''
import scrapy
from mySpider.items import LushiItem

class LushiSpider(scrapy.Spider):
    name = 'lushi'
    allowed_domains = ['duowan.com']
    start_urls = ['http://db.duowan.com/lushi/']
    url = 'http://db.duowan.com/lushi/'
    page_offset = 1#第一页
    page_total = 15;

    def parse(self, response):
        print('aaaaaaaaaaaaa')
        print(response)
        #print(response.xpath('//table[contains(@class,"table-s3")]/tbody/tr'))
        for sel in response.xpath('//table[contains(@class,"table-s3")]/tbody/tr'):
            item = LushiItem()
            name = sel.xpath('td[contains(@class,"name")]/a/text()').extract()
            img  = sel.xpath('td[contains(@class,"name")]/a/@data-src').extract()
            skill= sel.xpath('td[contains(@class,"skill")]/a/@data-tips').extract()
            txt  = sel.xpath('td[contains(@class,"txt")]/text()').extract()
            job  = sel.xpath('td[4]/text()').extract()
            type = sel.xpath('td[5]/text()').extract()
            Mana = sel.xpath('td[6]/text()').extract()
            attack = sel.xpath('td[7]/text()').extract()
            health = sel.xpath('td[8]/text()').extract()
            item['name'] = name
            yield item
        next_page_url = response.xpath('//a[contains(@rel,"next")]/@href').extract()
        print(next_page_url)
        if(self.page_offset<=self.page_total):
            self.url = 'http://db.duowan.com/lushi/card/list/eyJwIjoyLCJzb3J0IjoiaWQuZGVzYyJ9.html'
            self.page_offset = 2
            yield scrapy.Request(self.url,callback=self.parse)

            #yieldprint(attack) item

