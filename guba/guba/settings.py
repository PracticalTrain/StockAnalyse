# -*- coding: utf-8 -*-

# Scrapy settings for guba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import sys
import os
import django
sys.path.append('../../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PracticalTraining.settings'
django.setup()

COOKIES_ENABLED = False  # 禁用cookies
DOWNLOAD_DELAY = 30  # 延迟下载
BOT_NAME = 'guba'

SPIDER_MODULES = ['guba.spiders']
NEWSPIDER_MODULE = 'guba.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'guba (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [
    {'ip_port': '123.65.217.151:9797', 'user_pass': ''},
    {'ip_port': '60.206.148.135:3128', 'user_pass': ''},
    {'ip_port': '123.57.180.234:3128', 'user_pass': ''},
    {'ip_port': '219.238.124.221:3128', 'user_pass': ''},
    {'ip_port': '218.103.60.205:8080', 'user_pass': ''},
    {'ip_port': '183.131.76.27:8888', 'user_pass': ''},
    {'ip_port': '60.21.209.114:8080', 'user_pass': ''},
    {'ip_port': '121.40.108.76:8123', 'user_pass': ''},
    {'ip_port': '222.33.192.238:8118', 'user_pass': ''},

]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '55',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # # 'Cookie': 'LGMOID=20161118201632-7AECCDB0BA501409E62AFEA8403EB279; user_trace_token=20161118201635-5bcca64725174f78b0b9c99e24a9b4af; LGUID=20161118201635-d937fc2f-ad88-11e6-b364-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=D5935BB3E47293ED612631DF9EFE6040; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DyGPqGmsCs2FdOLEsxSgIrYAnWuK1R03bw9X0LlXsoau%26wd%3D%26eqid%3De52a9a5d000162ec00000002583938a2; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1479472421,1480066055,1480145069,1480145217; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1480145224; _ga=GA1.2.1114641428.1479471393; LGSID=20161126152433-6102796c-b3a9-11e6-b20a-5254005c3644; LGRID=20161126152709-bd995fd7-b3a9-11e6-b20a-5254005c3644; SEARCH_ID=04a6b755707e4918b1476c552cfe8694',
    # 'Host': 'www.lagou.com',
    # 'Origin': 'https://www.lagou.com',
    # 'Referer': 'https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91?px=default&city=%E5%8C%97%E4%BA%AC',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    # 'X-Anit-Forge-Code': '0',
    # 'X-Anit-Forge-Token': 'None',
    # 'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'guba.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = 'd62054fa06384d2d94ac1189e629c758'
# CRAWLERA_PASS = 'vs7452014'
#
# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600
#
# CRAWLERA_PRESERVE_DELAY = True
#
DOWNLOADER_MIDDLEWARES = {
    # 'guba.middlewares.ProxyMiddleware': 543,
    # 'guba.middlewares.RandomUserAgent': 600,
    #  'scrapy_crawlera.CrawleraMiddleware': 600
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'guba.pipelines.GubaPipeline': 300,
    'guba.pipelines.LagouPipeline': 300,
    'guba.pipelines.GubaYaowenPipeline': 300,
    'guba.pipelines.LagouUrlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
