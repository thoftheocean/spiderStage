# !/usr/bin/env python
# coding:utf-8
# author hx

import urllib2

if __name__ == '__main__':
    # 设置request的URL信息和头部信息
    url = "http://www.baidu.com"
    # 设置头部
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    request = urllib2.Request(url=url, headers=headers)
    # 发送请求和接收响应
    response = urllib2.urlopen(request)
    print(response.read())


