# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/']

    def parse(self, response):

        #1将响应的源代码写入html文件中
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # #item提取内容
        # for quote in response.css('div.quote'):
        #     yield{
        #         'text':quote.css('span.text::text').extract_first(),
        #         'tags':quote.css('div.tags a.tag::text').extract()
        #     }

        #item提取内容
        items=[]
        for quote in response.css('div.quote'):
            item=TutorialItem()
            item['text']=quote.css('span.text::text').extract_first()
            item['tags']=quote.css('div.tags a.tag::text').extract()
            items.append(item)
        return items



