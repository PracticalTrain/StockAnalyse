# -*- encoding:utf-8 -*-
__author__ = 'jjzhu'

import random
import urllib
import base64
from .settings import PROXIES
import requests
import json


class RandomUserAgent(object):
    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '55',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'LGMOID=20161118201632-7AECCDB0BA501409E62AFEA8403EB279; user_trace_token=20161118201635-5bcca64725174f78b0b9c99e24a9b4af; LGUID=20161118201635-d937fc2f-ad88-11e6-b364-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=D5935BB3E47293ED612631DF9EFE6040; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DyGPqGmsCs2FdOLEsxSgIrYAnWuK1R03bw9X0LlXsoau%26wd%3D%26eqid%3De52a9a5d000162ec00000002583938a2; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1479472421,1480066055,1480145069,1480145217; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1480145224; _ga=GA1.2.1114641428.1479471393; LGSID=20161126152433-6102796c-b3a9-11e6-b20a-5254005c3644; LGRID=20161126152709-bd995fd7-b3a9-11e6-b20a-5254005c3644; SEARCH_ID=04a6b755707e4918b1476c552cfe8694',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        # 'Referer': 'https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        }
    """Randomly rotate user agents based on a list of predefined ones"""
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # print "**************************" + random.choice(self.agents)
        # agent = random.choice(self.agents)
        open('request_header', 'w').write(str(request.headers))
        agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        request.headers.setdefault('User-Agent', agent)


class ProxyMiddleware(object):
    def __init__(self):
        #  = requests.get('http://127.0.0.1:8000/?types=0&count=60&country='+urllib.quote('中国'))
        # ip_ports = json.loads(result.text)
        self.available_ips = ['http://115.29.76.108:8088',
                              'http://115.196.155.37:8998',
                              'http://121.232.145.98:9000',
                              'http://36.97.143.28:9999']
        # for ip_port in ip_ports:
        # self.available_ips.append('http://%s:%d' % (ip_port['ip'], ip_port['port']))
        # self.available_ips.append('http://%s:%d' % (ip_port['ip'], ip_port['port']))

    def process_request(self, request, spider):
        proxy = random.choice(self.available_ips)
        print proxy
        request.meta['proxy'] = proxy

