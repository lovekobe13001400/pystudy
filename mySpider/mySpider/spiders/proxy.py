# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ProxyItems

class ProxySpider(scrapy.Spider):
    name = 'proxy'
    custom_settings = {
        'ITEM_PIPELINES': {'mySpider.pipelines.ProxySqlPipeLine': 300},
    }
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']
    page = 1
    page_total = 1000
    def parse(self, response):
        for sel in response.xpath('//table/tbody/tr'):
            item = ProxyItems()
            item['ip'] = sel.xpath('td[1]/text()').extract()
            item['port']= sel.xpath('td[2]/text()').extract()
            item['speed'] = sel.xpath('td[6]/text()').extract()
            yield item
        self.page += 1
        if(self.page<=self.page_total):
            print(self.page)
            self.url = 'https://www.kuaidaili.com/free/inha/%s/'%(self.page)
            yield scrapy.Request(self.url,callback=self.parse)