__author__ = 'jjzhu'
from scrapy.spider import Spider
import scrapy
import urllib
import json
from ..items import UrlItem


class LagouPreSpider(Spider):
    name = 'lagou_pre'
    allowed_domains = ['www.lagou.com']
    url_str = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false'
    pipelines = ['LagouUrlPipeline']

    def start_requests(self):
        for position in open('positions.txt', 'r'):
            if position.strip() == '':
                continue
            for city in open('cities.txt', 'r'):
                if city.strip() == '':
                    continue
                url = self.url_str % urllib.quote(city.strip())
                form_data = {'first': 'true', 'pn': str(1), 'kd': position.strip()}
                yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        return_json = json.loads(response.body.decode(encoding='utf-8'))
        content = return_json['content']
        page_size = content['pageSize']
        position_result = content['positionResult']
        city = position_result['locationInfo']['city']
        kind = position_result['queryAnalysisInfo']['positionName']
        total_count = position_result['totalCount']
        total_page = total_count/page_size + (0 if total_count % page_size == 0 else 1)

        item = UrlItem()
        item['url'] = response.url
        item['page_size'] = page_size
        item['page_count'] = total_page
        item['kind'] = kind if kind is not None else ''
        item['city'] = city if city is not None else ''
        yield item
