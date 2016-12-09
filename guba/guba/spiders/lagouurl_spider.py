__author__ = 'jjzhu'
from scrapy.spider import Spider
import scrapy


class LagouUrlSpider(Spider):
    name = 'lagou_url'
    allowed_domains = ['www.lagou.com']
    start_urls = [
        'https://www.lagou.com/',
        'https://www.lagou.com/zhaopin/Java/?labelWords=label',
    ]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def parse(self, response):
        positions = response.xpath("//div[@id='sidebar']/div[@class='mainNavs']/div/div/dl/dd/a/text()").extract()
        position_file = open('positions.txt', mode='w', encoding='utf-8')
        for position in positions:
            print position
            position_file.write(('\''+position+'\',\n').decode(encoding='gbk'))
        position_file.close()
        yield scrapy.Request(self.start_urls[1], callback=self.parse_city)

    def parse_city(self, response):
        cities = response.xpath('//div[@id="filterCollapse"]/div[@class="has-more"]/div/li/a/text()').extract()[1:-1]
        city_file = open('cities.txt', mode='w')
        for city in cities:
            print city
            city_file.write((city+'\n').decode(encoding='gbk'))
        city_file.close()