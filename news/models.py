from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1000, default='')
    pub_time = models.CharField(max_length=20)
    source = models.CharField(max_length=50, default='')
    content = models.TextField(null='')
    abstract = models.TextField(default='')
