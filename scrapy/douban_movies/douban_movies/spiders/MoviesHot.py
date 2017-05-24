# -*- coding: utf-8 -*-
import scrapy
from douban_movies.items import DoubanMoviesItem
import json
class MovieshotSpider(scrapy.Spider):

    name = "MoviesHot"
    allowed_domains = ["douban.com"]
    i=0
    start_urls = []
    while i <=40:
		#i最大值可以取320
        url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(i)
        start_urls.append(url)
        i +=20
    # start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
    #               'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20']
    def parse(self, response):
        # with open('hot.json', 'wb') as f:
        #     f.write(response.body)
        # print  response.body
        content = json.loads(response.body)

        # print content
        for movie in content['subjects']:
            # print movie
            item = DoubanMoviesItem()
            item['name'] = movie['title']
            item['score'] = movie['rate']
            item['cover'] = movie['cover']
            item['info_url'] = movie['url']
            print item

            yield scrapy.Request(url=item["info_url"], meta={'item': item}, callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):

        div = response.xpath('//div[@id="info"]')
        item = response.meta['item']

        item["directer"] = div.xpath("span[1]/span[2]/a/text()").extract()[0]
        item["actors"] = div.xpath('span[3]/span/a/text()').extract()
        # print item["actors"]
        #strip()去除文本中开头和末尾的空格
        item['info'] = response.xpath('//*[@id="link-report"]/span[1]/text()').extract()[0].strip()
        yield item

