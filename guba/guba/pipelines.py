# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from lagou.models import BBS, Position


class GubaPipeline(object):
    NAME = 'GubaPipeline'

    def process_item(self, item, spider):

        if self.NAME not in getattr(spider, 'pipelines', []):
            return item
        # print item['owner'], item['title'], item['time_way']
        print self.NAME + '-'*10
        bbs = BBS(owner=item['owner'], title=item['title'], time_way=item['time_way'])
        bbs.save()
        return item


class LagouPipeline(object):
    NAME = 'LagouPipeline'

    def process_item(self, item, spider):
        # print item['owner'], item['title'], item['time_way']
        print self.NAME + '-'*10
        if self.NAME not in getattr(spider, 'pipeline', []):
            return item
        print '-' * 100
        for p in item['result_json_str']:
            position = Position()
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