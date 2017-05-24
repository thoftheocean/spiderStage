# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem

class GetipsSpider(scrapy.Spider):
    name = "getips"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com']

    #获取多个网址的响应
    def start_requests(self):
        reqs = []
        for i in range(1, 206):
             req= scrapy.Request("http://www.xicidaili.com/nn/%s" % i)
        reqs.append(req)
        return reqs

    def parse(self, response):

        ip_list = response.xpath('//table[@id="ip_list"]/tr[@class="odd"]')

        for ip in ip_list:

            pre_item = CollectipsItem()
            pre_item['ip']=ip.xpath('td[2]/text()').extract()[0]
            pre_item['port'] = ip.xpath('td[3]/text()').extract()[0]
            pre_item['type'] = ip.xpath('td[6]/text()').extract()[0]
            pre_item['position'] = ip.xpath('td[4]/a/text()').extract()[0]
            pre_item['speed'] = ip.xpath('td[7]/div/@title').re('\d{0,2}\.\d{0,}')[0]

            yield pre_item




