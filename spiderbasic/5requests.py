# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import requests

def get_json():
    r = requests.get('http://api.github.com/events')
    print (r.status_code)
    print (r.headers)
    print (r.content)
    print (r.text)
    print (r.json())

def get_queystring():
    url = 'http://httpbin.org/get'
    params = {'qs1':'value1','qs2':'value2'}
    r = requests.get(url=url,params=params)
    print (r.status_code)
    print (r.content)

def get_custom_headers():
    url = 'http://httpbin.org/get'
    headers = {'x-headers1':'value1','x-headers2':'value2'}
    r = requests.get(url=url,headers=headers)
    print (r.status_code)
    print (r.content)

def get_cookie():
    headers = {'User-Agent':'Chrome'}
    url = 'http://douban.com'
    r = requests.get(url=url, headers=headers)
    print (r.status_code)
    print (r.cookies)
    print (r.cookies['bid'])


if __name__ == "__main__":
    # get_json()
    # get_queystring()
    # get_custom_headers()
    get_cookie()