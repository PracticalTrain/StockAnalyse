# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BBS(models.Model):
    title = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    time_way = models.CharField(max_length=100)


class Position(models.Model):
    position_id = models.CharField(max_length=20)
    first_type = models.CharField(max_length=50, default='')
    second_type = models.CharField(max_length=50)
    company_id = models.CharField(max_length=20)

    city = models.CharField(max_length=50, null=True)  # 城市
    positionName = models.CharField(max_length=50, null=True)  # 职位
    companyFullName = models.CharField(max_length=100, null=True)  # 公司全称
    companySize = models.CharField(max_length=20, null=True)  # 公司人数规模
    createTime = models.CharField(max_length=30, null=True)  # 职位发布时间
    district = models.CharField(max_length=30, null=True)  #
    education = models.CharField(max_length=20, null=True)  # 学历要求
    industryField = models.CharField(max_length=50, null=True)
    salary = models.CharField(max_length=20, null=True)  # 年薪
    workYear = models.CharField(max_length=10, null=True)  # 工作时间
    financeStage = models.CharField(max_length=20, null=True)  #
    jobNature = models.CharField(max_length=10, null=True)  # 工作类型


class PositionDetail(models.Model):
    position_id = models.CharField(max_length=20, primary_key=True)
    advantage = models.CharField(max_length=500, null='')
    description = models.TextField(null='')
    address = models.TextField(null='')


class Url(models.Model):
    url = models.CharField(max_length=200, default='')
    page_size = models.IntegerField(default=0)
    page_count = models.IntegerField(default=0)
    kind = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=20, default='')

    def __str__(self):
        return 'kind:%s, city:%s, page_size:%s, page_count:%s' % (self.kind, self.city, self.page_size, self.page_count)