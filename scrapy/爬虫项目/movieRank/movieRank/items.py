# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovierankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    info_url = scrapy.Field()
    # img_url =scrapy.Field()
    directer= scrapy.Field()
    actors = scrapy.Field()
    date = scrapy.Field()
    runtime = scrapy.Field()
    info = scrapy.Field()