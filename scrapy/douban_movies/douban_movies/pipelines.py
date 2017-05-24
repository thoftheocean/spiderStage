# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import urllib

class DoubanMoviesPipeline(object):

    def process_item(self, item, spider):

        if not os.path.isdir('movies'):
            os.mkdir('movies')
        if not os.path.isdir('movies/'+item['name']):
            os.mkdir('movies/'+item['name'])

        filename = 'movies/'+item['name']+'/'+item['name']+'.txt'
        with open(filename, 'w+') as f:
            actors=''
            for actor in item['actors']:
                actors += actor+'|'
            info = '电影名：%s\n导演：%s\n主演：%s\n评分：%s\n简介：%s'%(item['name'],item['directer'],actors,item['score'],item['info'])
            f.write(info)
        #下载图片

        urllib.urlretrieve(item['cover'], 'movies/'+item['name']+'/'+item['name']+'.jpg')

