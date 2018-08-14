# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
import time
from mySpider import MysqlHelper
class MyspiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        self.file = open('teacher.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(bytes(content, encoding = "utf8"))
        return item

    def close_spider(self, spider):
        self.file.close()


class MysqlPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        self.file = open('teacher.json', 'wb')

    def process_item(self, item, spider):
        name = item['name']
        img = item['img']
        price = item['price']

        sql = 'insert into goods values(null,%(name)s,%(img)s,%(price)s)'
        params = {"name":name,"img":img,"price":price}
        helper = MysqlHelper.MysqlHelper('localhost', 3306, 'test', 'root', 'root')
        url = 'https://a-ssl.duitang.com/uploads/item/201605/24/20160524132459_h4LRn.thumb.700_0.jpeg'


        urllib.request.urlretrieve(url, './mySpider/images/1.jpg')
        #helper.insert(sql,params)
        return item

    def close_spider(self, spider):
        self.file.close()

#腾讯招聘
class TencentJsonPipeline(object):

    def __init__(self):
        #self.file = open('teacher.json', 'wb')
        self.file = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(bytes(content, encoding="utf8"))
        return item

    def close_spider(self, spider):
        self.file.close()
class StockJsonPipeline(object):
    def __init__(self):
        # self.file = open('teacher.json', 'wb')
        self.file = open('stock.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(bytes(content, encoding="utf8"))
        return item

    def close_spider(self, spider):
        self.file.close()

#
class StockSqlPipeLine(object):
    def __init__(self):
        self.helper = MysqlHelper.MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
        #self.file = open('teacher.json', 'wb')

    def process_item(self, item, spider):
        sid = item['sid']
        gn_name = item['gn_name']
        url_code = item['url_code']
        sql = 'insert into tan_plate values(null,%(sid)s,%(gn_name)s,%(url_code)s)'
        params = {"sid": sid, "gn_name": gn_name, "url_code": url_code}

        self.helper.insert(sql, params)

    def close_spider(self, spider):
        pass
        #self.file.close()


class ProxySqlPipeLine(object):
    def __init__(self):
        self.helper = MysqlHelper.MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
        # self.file = open('teacher.json', 'wb')

    def process_item(self, item, spider):
        ip = item['ip']
        port = item['port']
        speed = item['speed']
        sql = 'insert into tan_proxy values(null,%(ip)s,%(port)s,%(speed)s,0)'
        params = {"ip": ip, "port": port, "speed": speed}

        self.helper.insert(sql, params)

    def close_spider(self, spider):
        pass
        # self.file.close()
class ReportSqlPipeLine(object):
    def __init__(self):
        self.helper = MysqlHelper.MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
        # self.file = open('teacher.json', 'wb')

    def process_item(self, item, spider):
        sid = item['sid']
        sname = item['sname']
        time_date = item['time_date']
        yy_tb = float(item['yy_tb'])
        yy_hb = float(item['yy_hb'])
        lr_tb = float(item['lr_tb'])
        lr_hb = float(item['lr_hb'])
        sql = 'insert into tan_report values(null,%(sid)s,%(sname)s,%(time_date)s,%(yy_tb)s,%(yy_hb)s,%(lr_tb)s,%(lr_hb)s)'
        params = {
            "sid": sid,
            "sname": sname,
            'time_date':time_date,
            "yy_tb": yy_tb,
            "yy_hb": yy_hb,
            "lr_tb": lr_tb,
            "lr_hb": lr_hb
        }
        print(params)

        self.helper.insert(sql, params)

    def close_spider(self, spider):
        pass