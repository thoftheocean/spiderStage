# -*- coding: utf-8 -*-
import scrapy
from movieRank.items import MovierankItem

class RankSpider(scrapy.Spider):
    name = "rank"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):

        with open('rank.html', 'wb') as f:
            f.write(response.body)

        for div in response.xpath('//a[@class="nbg"]'):
            item = MovierankItem()
            item['name'] = div.xpath('@title')[0].extract()
            item['info_url'] = div.xpath('@href')[0].extract()
            # item['img_url'] = div.xpath('img/@src')[0].extract()

            # info_url = div.xpath('@href')[0].extract()
            # item["info_url"] = info_url if "http:" in info_url else ("http:" + info_url)

            yield scrapy.Request(url=item["info_url"], meta={'item': item}, callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):

        div = response.xpath('//div[@id="info"]')

        # if not div:
        #     self.log("Detail Page error--%s" % response.url)

        item = response.meta['item']
        item["directer"] = div.xpath("span[1]/span[2]/a/text()").extract()
        item["actors"] = div.xpath("span[3]/span[2]/span/a/text()").extract()
        item["date"] = div.xpath("span[12]/@content").extract()
        item["runtime"] = div.xpath("span[14]/text()").extract()
        item['info']= response.xpath('//*[@id="link-report"]/span[1]/text()').extract()

        yield item
