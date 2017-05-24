# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    cover = scrapy.Field()
    info_url=scrapy.Field()
    directer = scrapy.Field()
    actors = scrapy.Field()
    info = scrapy.Field()
