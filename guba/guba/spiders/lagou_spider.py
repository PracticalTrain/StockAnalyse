# -*- encoding:utf-8 -*-
__author__ = 'jjzhu'
from scrapy.spiders import Spider, BaseSpider
import scrapy.http
import scrapy
import json
import re
import random
from ..items import PositionItem, PositionDetailItem
from lagou.models import Url


class LagouSpider(Spider):
    name = 'lagou'
    allowed_domains = ['https://www.lagou.com']
    start_urls = [
        'https://www.lagou.com',
    ]
    position_info_url = 'https://www.lagou.com/jobs/%s.html'
    pipelines = 'LagouPipeline'
    urls = Url.objects.all().filter(page_count__gte=1)[1:20]

    def start_requests(self):
        yield scrapy.http.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):

        all_jobs = []
        f = open('jobs.txt', 'w')
        for u in self.urls:
            url = u.url
            page_count = int(u.page_count)
            kind = u.kind
            job = {}
            for pn in range(page_count):
                job['url'] = url
                job['form_data'] = {'pn': str(pn + 1), 'kd': kind}
                all_jobs.append(job)
                f.write(str(job)+'\n')
                f.flush()
            u.delete()
        # random.shuffle(all_jobs)

        for job in all_jobs:
            # del job['form_data']['city']
            yield scrapy.http.FormRequest(url=job['url'], formdata=job['form_data'],
                                          callback=self.parse_position, dont_filter=True, )
            # open('0.txt', 'a').write('url:%s, form_data:%s\n' % (url, form_data))
            # yield scrapy.FormRequest(url=response.url, formdata=form_data, callback=self.parse_position)

    def parse_position(self, response):
        return_json = json.loads(response.body.decode(encoding='utf-8'))
        result = return_json['content']['positionResult']['result']
        item = PositionItem()
        item['result_json_str'] = result
        if len(result) == 0:
            open('failed.txt', 'a').write(response.url+'\n')

        yield item
        # for job in result:
        #     url = self.position_info_url % str(job['positionId'])
        #     yield scrapy.Request(url=url, callback=self.parse_position_detail, dont_filter=True)

    def parse_position_detail(self, response):
        print '-'*100
        job_detail = response.xpath('//dl[@id="job_detail"]')
        advantage = job_detail.xpath('dd[@class="job-advantage"]/p/text()').extract()[0]
        description_sentences = job_detail.xpath('dd[@class="job_bt"]/div/p/text()').extract()
        description = '\n'.join(description_sentences)
        work_addr_a = response.xpath('//div[@class="work_addr"]/a/text()').extract()
        address = '_'.join(work_addr_a)
        item = PositionDetailItem()
        item['detail_dict'] = {
            'advantage': advantage,
            'description': description,
            'address': address,
            'position_id': re.findall('\d+', response.url)[0]
        }
        yield item