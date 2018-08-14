# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ReportItems

class ReportSpider(scrapy.Spider):
    name = 'report'
    allowed_domains = ['10jqka.com']
    start_urls = ['http://data.10jqka.com.cn/ajax/yjgg/date/2018-03-31/board/ALL/field/DECLAREDATE/order/desc/page/7/ajax/1/']
    custom_settings = {
        'ITEM_PIPELINES': {'mySpider.pipelines.ReportSqlPipeLine': 300},
    }
    def parse(self, response):
        item = ReportItems()
        for sel in response.xpath('//table/tbody/tr'):
            item['sid'] = sel.xpath('td[2]/a/text()').extract()[0]
            item['sname'] = sel.xpath('td[3]/a/text()').extract()[0]
            item['time_date'] = sel.xpath('td[4]/text()').extract()[0]
            item['yy_tb'] = sel.xpath('td[6]/text()').extract()[0]
            item['yy_hb'] = sel.xpath('td[6]/text()').extract()[0]
            item['lr_tb'] = sel.xpath('td[6]/text()').extract()[0]
            item['lr_hb'] = sel.xpath('td[6]/text()').extract()[0]
            yield item
        next_page_url = response.xpath('//a[contains(@rel,"next")]/@href').extract()
        print(next_page_url)
        if (self.page_offset <= self.page_total):
            self.url = 'http://db.duowan.com/lushi/card/list/eyJwIjoyLCJzb3J0IjoiaWQuZGVzYyJ9.html'
            self.page_offset = 2
            yield scrapy.Request(self.url, callback=self.parse)
