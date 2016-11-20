python manage.py startapp APP_NAME
python manage.py runserver（host:port） 启动服务
数据库同步三部曲
python manage.py makemigrations APP_NAME
python manage.py sqlmigrate APP_NAME 0001
python manage.py migrate
连接mysql
setting.py中修改配置

DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'finance_ana',
        'USER': 'root',
        'PASSWORD': '111111',
        'PORT': 3306,
    }
}

再安装MysqlDB
http://www.codegood.com/downloads下载对应的库
python ImportError: DLL load failed: %1 不是有效的 Win32 应用程序
这个是因为你安装了64位的python，然后安装32位的mysql模块，或者你安装了32位的python，然后安装64位的myql模块
-------
UnicodeDecodeError: 'ascii' codec can't decode byte 0xb0 in position 1: ordinal not in range(128)
加上如下代码
reload(sys)
sys.setdefaultencoding('gbk')
编码格式的问题

PYTHON_HOME\Lib下的mimetypes.py，

pip install scrapy（安装scrapy）

  1. scrapy startproject tutorial  
  2. scrapy shell website
  3. scrapy crawl NAME 
  4. scrapy crawl NAMME -o items.json -t json  

scrapy djangoitem 插件
https://github.com/scrapy-plugins/scrapy-djangoitem

在爬虫项目中setting.py添加

```
import sys
import os
import django
sys.path.append('../../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PracticalTraining.settings'
django.setup()

```
django.setup() 不加会报错

Apps aren't loaded yet

去掉ITEM_PIPELINES的注释

```
ITEM_PIPELINES = {
    'guba.pipelines.GubaPipeline': 300,
}
```

修改


```
class GubaPipeline(object):

	def process_item(self, item, spider):

        # print item['owner'], item['title'], item['time_way']
        # print '-'*10
        bbs = BBS(owner=item['owner'], title=item['title'], time_way=item['time_way'])
        bbs.save()
        return item
```