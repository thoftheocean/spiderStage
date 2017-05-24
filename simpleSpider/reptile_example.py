# !/usr/bin/env python
# coding:utf-8
# author hx
import urllib
import urllib2
import re
# 抓取糗事百科上面的文字
if __name__=='__main__':
    # 抓取过程
    # 1访问其中一个网页地址，获取源代码
    url = 'http://www.qiushibaike.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)
    content=response.read()
    # 2根据抓取的网页源代码，提取数据
    regex = re.compile('<div class="content">(.*?)<!--(.*?)-->.*?</div>', re.s) #加了re.s之后就会.也可以输出换行
    print re.findall(regex, content)
    # 保存抓取的数据
    # 抓取剩下的网页的数据