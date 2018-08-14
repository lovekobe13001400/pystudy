# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
    pass

class LushiItem(scrapy.Item):
    name = scrapy.Field()

class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()

class StockItem(scrapy.Item):
    sid = scrapy.Field()
    gn_name = scrapy.Field()
    url_code = scrapy.Field()

class StockPointItem(scrapy.Item):
    gn_name = scrapy.Field()
    zdf = scrapy.Field()
    sid = scrapy.Field()



class ProxyItems(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    speed = scrapy.Field()
    pass

class ReportItems(scrapy.Item):
    sid = scrapy.Field()
    sname = scrapy.Field()
    time_date = scrapy.Field()
    yy_tb = scrapy.Field()
    yy_hb = scrapy.Field()
    lr_tb = scrapy.Field()
    lr_hb = scrapy.Field()

