# !/usr/bin/env python
# coding:utf-8
# author hx

import urllib
import urllib2

if __name__ == '__main__':
    # 设置request的URL信息和头部信息
    url = "http://www.maiziedu.com/user/login/"
    # 设置头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    values = {'email': '15680236583', 'pwd': '123456'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url=url, data=data, headers=headers)
    # 发送请求和接收响应
    response = urllib2.urlopen(request)
    print response.read()

