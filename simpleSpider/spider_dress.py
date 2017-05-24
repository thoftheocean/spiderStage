# !/usr/bin/env python
# encoding:utf-8
# author:hx
# import urllib2
import requests
import re
import json
url ='https://s.taobao.com/search?q=%连衣裙'
res = requests.get(url)
con = res.content
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
# request = urllib2.Request(url=url, headers=headers)
# response = urllib2.urlopen(request)
# con = response.read()
g_page = re.findall(re.compile('g_page_config =(.+)'), con)
# print g_page
# print g_page[0]
# print g_page[0:-1]
dict_json = json.loads(g_page[0][0:-1])
print dict_json
item_list = dict_json['mods']['itemlist']['data']['auctions']
for item in item_list:
    print item['raw_title']
    print item['nick']
    print item['view_price']
    print item['pic_url']
    print '='*30

