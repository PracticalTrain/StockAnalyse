# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BBSItem(scrapy.Item):
    title = scrapy.Field()
    owner = scrapy.Field()
    time_way = scrapy.Field()


class PositionItem(scrapy.Item):
    result_json_str = scrapy.Field()