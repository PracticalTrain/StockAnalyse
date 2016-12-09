# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from lagou.models import BBS, Position, Url, PositionDetail
from news.models import News
from .items import PositionItem, PositionDetailItem


class GubaPipeline(object):
    NAME = 'GubaPipeline'

    def process_item(self, item, spider):

        if self.NAME not in getattr(spider, 'pipelines', []):
            return item
        # print item['owner'], item['title'], item['time_way']
        bbs = BBS(owner=item['owner'], title=item['title'], time_way=item['time_way'])
        bbs.save()
        return item


class LagouPipeline(object):
    NAME = 'LagouPipeline'

    def process_item(self, item, spider):
        # print item['owner'], item['title'], item['time_way']

        if self.NAME not in getattr(spider, 'pipelines', []):
            return item
        if isinstance(item, PositionDetailItem):
            print '*'*50 + '  PositionDetailItem  '+self.NAME + '*'*50
            detail = PositionDetail()
            result = item['detail_dict']
            detail.position_id = result['position_id']
            detail.address = result['address']
            detail.advantage = result['advantage']
            detail.description = result['description']
            detail.save()
        elif isinstance(item, PositionItem):

            print '*'*50 + '  PositionItem  '+self.NAME + '*'*50
            for p in item['result_json_str']:
                position = Position()
                position.position_id = p['positionId']
                position.company_id = p['companyId']
                position.first_type = p['firstType']
                position.second_type = p['secondType']

                position.city = p['city']  # 城市
                position.positionName = p['positionName']
                position.companyFullName = p['companyFullName']
                position.companySize = p['companySize']
                position.createTime = p['createTime']
                position.district = p['district']
                position.education = p['education']
                position.industryField = p['industryField']
                position.salary = p['salary']
                position.workYear = p['workYear']
                position.financeStage = p['financeStage']
                position.jobNature = p['jobNature']
                position.save()
        return item


class LagouUrlPipeline(object):
    NAME = 'LagouUrlPipeline'

    def process_item(self, item, spider):
        if self.NAME not in getattr(spider, 'pipelines', []):
            return item
        url_ = Url()
        url_.url = item['url']
        url_.kind = item['kind']
        url_.page_count = item['page_count']
        url_.page_size = item['page_size']
        url_.city = item['city']
        url_.save()
        return item

class GubaYaowenPipeline(object):
    NAME = 'GubaYaowenPipeline'

    def process_item(self, item, spider):
        # print item['owner'], item['title'], item['time_way']
        if self.NAME not in getattr(spider, 'pipelines', []):
            return item
        news = News()
        news.content = item['content']
        # news.editor = item['editor']
        news.pub_time = item['pub_time']
        news.source = item['source']
        news.title = item['title']
        news.abstract = item['abstract']
        news.save()
        return item