# -*- coding=utf-8 -*-
__author__ = 'jjzhu'

import scrapy
from scrapy.spiders import Spider, BaseSpider
from ..items import BBSItem


class GubaSpider(Spider):
    name = 'guba'
    allowed_domains = ['guba.eastmoney.com']
    root_domain = 'http://guba.eastmoney.com'
    start_urls = [
        "http://guba.eastmoney.com/list,600036.html",
    ]
    pipelines = ['GubaPipeline']

    def parse(self, response):
        article_list_news = response.xpath('//div[@id="articlelistnew"]/div')
        urls = []
        for article_new in article_list_news:
            href = article_new.xpath('span[@class="l3"]/a/@href').extract()
            if len(href) == 0 or href[0].startswith('http'):
                continue
            if href[0].startswith('/'):
                urls.append(self.root_domain + href[0])
            else:
                urls.append(self.root_domain + '/' + href[0])
            for url in urls:
                yield scrapy.Request(url, self.parse_bbs_detail)

    def parse_bbs_detail(self, response):
        print '*'*200
        owner = response.xpath('//div[@id=\'zwconttbn\']/strong/a/text()').extract()[0]  # 楼主
        time_way = response.xpath('//div[@id=\'zwconttb\']/div[@class=\'zwfbtime\']/text()').extract()[0]  # 时间
        title = response.xpath('//div[@id=\'zwconttbt\']/text()').extract()[0].strip()
        content_tag = response.xpath('//div[@id="zwconbody"]/div').extract()[0]
        item = BBSItem()
        item['title'] = title
        item['time_way'] = time_way
        item['owner'] = owner
        yield item

    def parse_company_detail(self, response):
        raise NotImplementedError()