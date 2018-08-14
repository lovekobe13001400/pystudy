# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['tt']
    start_urls = ['http://tt/']

    def parse(self, response):
        pass
