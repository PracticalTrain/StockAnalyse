# -*- coding:utf-8 -*-
__author__ = 'jjzhu'
from scrapy.spiders import Spider
import scrapy
import json
import urllib
from ..items import PositionItem

class LagouSpider(Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = [
        'https://www.lagou.com/jobs/positionAjax.json?city=',
    ]
    pipeline = 'LagouPipeline'

    def start_requests(self):
        url = self.start_urls[0] + urllib.quote('杭州')
        url.encode(encoding='utf-8')
        url.decode(encoding='utf-8')
        form_data = {'first': 'true', 'pn': str(1), 'kd': 'Java'}
        yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        url = self.start_urls[0] + urllib.quote('杭州')
        return_json = json.loads(response.body.decode(encoding='utf-8'))
        content = return_json['content']
        page_size = content['pageSize']
        position_result = content['positionResult']
        total_count = position_result['totalCount']
        total_page = total_count/page_size + (0 if total_count % page_size == 0 else 1)
        print total_count, total_page, page_size
        form_data = {'first': 'true', 'pn': str(1), 'kd': 'Java'}
        item = PositionItem()
        result = return_json['content']['positionResult']['result']
        item['result_json_str'] = result
        # yield item
        for pn in range(total_page):
            if pn == 0:
                form_data = {'first': 'true', 'pn': str(pn+1), 'kd': 'Java'}
            else:
                form_data = {'first': 'false', 'pn': str(pn+1), 'kd': 'Java'}

            yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_position)

    def parse_position(self, response):
        return_json = json.loads(response.body.decode(encoding='utf-8'))
        result = return_json['content']['positionResult']['result']
        item = PositionItem()
        item['result_json_str'] = result

        return item
