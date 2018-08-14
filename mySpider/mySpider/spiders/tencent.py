# -*- coding: utf-8 -*-
import scrapy
import re
from mySpider.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=30#a"
    ]

    def parse(self, response):
        for each in response.xpath('//*[@class="even" or @class="odd" ]'):
            item = TencentItem()
            item['name'] = each.xpath('./td[1]/a/text()').extract()
            item['detailLink'] = each.xpath('./td[1]/a/@href').extract()
            item['positionInfo'] = each.xpath('./td[2]/text()').extract()
            item['peopleNumber'] = each.xpath('./td[3]/text()').extract()
            item['workLocation'] = each.xpath('./td[4]/text()').extract()
            item['publishTime'] = each.xpath('./td[5]/text()').extract()



            
            # # 将获取的数据交给pipeline
            yield item


        #爬取下一页
        curpage = re.search('(\d+)', response.url).group(1)
        print(curpage)
        page = int(curpage) + 10
        url = re.sub('\d+', str(page), response.url)
        # # 发送新的url请求加入待爬队列，并调用回调函数 self.parse

        yield scrapy.Request(url, callback=self.parse)
    #获取简历详情
    def parse_content(self,response):
        title = response.xpath('//tr[@class="h"]/td/text()')
