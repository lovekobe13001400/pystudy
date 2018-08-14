# -*- coding: utf-8 -*-

# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#项目名称
BOT_NAME = 'mySpider'

SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'

#数据库配置
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'test'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'root'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
#如果启用，Scrapy会尊重robots.txt政策。有关详细信息，请参阅
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#激活管道罪案PIPELINES
#包含要使用的项目管道及其顺序的字典。顺序值是任意的，但通常将它们定义在0-1000范围内。较低订单处理较高订单前。
ITEM_PIPELINES = {
  #'mySpider.pipelines.MyspiderPipeline': 300,
 #'mySpider.pipelines.MysqlPipeline': 300,
 #'mySpider.pipelines.TencentJsonPipeline':300
 #'mySpider.pipelines.StockSqlPipeLine':300
 #'mySpider.pipelines.StockJsonPipeline': 300
#'mySpider.pipelines.IpProxyPoolPipeline': 300,
}
#爬取间隔
#下载器在从同一网站下载连续页面之前应等待的时间（以秒为单位）。这可以用于限制爬行速度，以避免击中服务器太难。支持小数。例：
DOWNLOAD_DELAY = 1
# 重写默认请求头
# DEFAULT_REQUEST_HEADERS = {
#  'Referer': 'http://q.10jqka.com.cn/gn/detail/code/300378/',
#  'Cookie':'spversion=20130314; historystock=000760%7C*%7C300383; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1528699762,1528875973,1528878574,1528942207; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1528948403; v=Ag0soJAFas3Nd87hRUPKBs8vHCKD6kG8yx6lkE-SSaQTRiNUFzpRjFtutWLc'
# }
# 禁用cookie
COOKIES_ENABLED = False
# DOWNLOADER_MIDDLEWARES = {
#     #'mySpider.middlewares.MyCustomDownloaderMiddleware': 543,
#     'mySpider.middlewares.RandomUserAgent': 1,
#     'mySpider.middlewares.RandomProxy': 100
# }
#激活自定义UserAgent和代理IP
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    #'mySpider.useragent.UserAgent': 1,
#    #'mySpider.proxymiddlewares.ProxyMiddleware':100,
#    #'scrapy.downloadermiddleware.useragent.UserAgentMiddleware' : None,
# }
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'









