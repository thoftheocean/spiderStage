# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import urllib
import urllib2
import cookielib

# #1urlopen
# def urlopen():
#     url = 'http://blog.kamidox.com'
#     try:
#         s = urllib2.urlopen(url, timeout=3)
#     except urllib2.URLError, e:
#         print (e)
#     else:
#         print (s.read(100))
#         s.close()
#
# if __name__ == '__main__':
#     urlopen()

# #2Request
# def request():
#     url = 'http://blog.kamidox.com'
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
#     req = urllib2.Request(url=url, headers=headers)
#     s = urllib2.urlopen(req)
#     print (s.read(100))
#     s.close()
#
# if __name__ == '__main__':
#     request()

# #1urllib2.build_opener
# def request_post_debug():
#     data = {'username': 'kamidox', 'password': '123456'}
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     req = urllib2.Request('http://www.douban.com', data=urllib.urlencode(data), headers=headers)
#     opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
#     s = opener.open(req)
#     print (s.read(100))
#     s.close
#
# if __name__ == '__main__':
#     request_post_debug()


# #2
# def request():
#     url = 'http://blog.kamidox.com'
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
#     req = urllib2.Request(url=url, headers=headers)
#     s = urllib2.urlopen(req)
#     print (s.read(100))
#     s.close()
#
# def install_debug_handler():
#     opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),
#                                   urllib2.HTTPHandler(debuglevel=2))
#     urllib2.install_opener(opener)
#
# if __name__ == "__main__":
#     install_debug_handler()
#     request()


def handle_cookie():
    cookiejar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler(debuglevel=1))
    s=opener.open('http://www.douban.com')
    print (s.read)
    s.close()

    s = opener.open('http://www.douban.com')
    s.close()

if __name__ == "__main__":
   handle_cookie()
