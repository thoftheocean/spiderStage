# -*- coding: utf-8 -*-


BOT_NAME = 'douban_movies'

SPIDER_MODULES = ['douban_movies.spiders']
NEWSPIDER_MODULE = 'douban_movies.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'douban_movies (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'douban_movies.RotateUserAgentMiddleware.RotateUserAgentMiddleware':400,
}

#下载延迟
DOWNLOAD_DELAY = 2

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   'douban_movies.pipelines.DoubanMoviesPipeline': 300,
}

LOG_FILE = "scrapy.log"