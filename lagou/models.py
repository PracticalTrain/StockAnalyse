# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BBS(models.Model):
    title = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    time_way = models.CharField(max_length=100)


class Position(models.Model):
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