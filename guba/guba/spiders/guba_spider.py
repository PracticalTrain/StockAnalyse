# -*- coding=utf-8 -*-
__author__ = 'jjzhu'

import scrapy
from scrapy.spiders import Spider, BaseSpider
from ..items import BBSItem, NewsItem
import time

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


class GubaYaowenSpider(Spider):
    name = 'gubayaowen'
    allowed_domains = ['guba.eastmoney.com', 'finance.eastmoney.com']
    start_urls = [
        "http://finance.eastmoney.com/yaowen.html",
    ]
    done_urls = set()
    pipelines = ['GubaYaowenPipeline']

    def start_requests(self):
        yield self.make_requests_from_url(self.start_urls[0])

    def parse(self, response):
        artitile_list = response.xpath('//div[@id="artitileList1"]/ul/li[contains(@id, "newsTr")]')
        urls = []
        for artitile in artitile_list:
            href = artitile.xpath('div/p/a/@href').extract()
            if len(href) == 0:
                continue
            urls.append(href[0])
            for url in urls:
                if url in self.done_urls:
                    print '%s has been parsed' % url
                    continue
                self.done_urls.add(url)
                yield scrapy.Request(url, self.parse_news, dont_filter=True)

        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, dont_filter=True)

    def parse_news(self, response):
        news_content = response.xpath("//div[@class='newsContent']")
        title = news_content.xpath('h1/text()').extract()[0]
        time_source = news_content.xpath('div[@class="Info"]/div[@class="time-source"]')
        pub_time = time_source.xpath('div[@class="time"]/text()').extract()[0]
        source = time_source.xpath('div[@class="source"]/img/@alt').extract()[0]
        abstract = news_content.xpath("div[@id='ContentBody']/div[@class='b-review']/text()").extract()[0]
        content = news_content.xpath("div[@id='ContentBody']").extract()[0]
        item = NewsItem()
        item['title'] = title
        item['pub_time'] = pub_time
        item['source'] = source
        item['abstract'] = abstract
        item['content'] = content.replace('\r\n', '<br>')
        yield item

    def parse_company_detail(self, response):
        raise NotImplementedError()
