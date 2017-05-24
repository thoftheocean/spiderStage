# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import urllib
import urlparse
#case 1 read 和readline

# def demo():
#     s = urllib.urlopen('https://www.douban.com/people/127746074/')
#     # print(s.read(100)) #打印100个字节
#     print(s.readline())  # 打印一行信息
# if __name__ == "__main__":
#     demo()

#case 2 readlines
# def print_list(list):
#     for i in list:
#         print(i)
#
# def demo():
#     s = urllib.urlopen('https://www.douban.com/people/127746074/')
#     print_list(s.readlines()) #以列表的形式进行打印
# if __name__ == "__main__":
#     demo()

# #HTTPmessage
# def print_list(list):
#     for i in list:
#         print(i)
# def demo():
#     s = urllib.urlopen('https://www.douban.com/people/127746074/')
#     msg = s.info()
#     # print_list(msg.headers)
#     # print_list(msg.items()) #获取每个head然后以元组方式显示
#     print(msg.getheader('Content-Type')) #获取某个具体的头
# if __name__ == "__main__":
#     demo()


# #case4
# def print_list(list):
#     for i in list:
#         print(i)
# def demo():
#     s = urllib.urlopen('https://www.douban.com/people/127746074/')
#     msg = s.info()
#     print_list(dir(msg))  #获取msg对象里面的方法
#
# if __name__ == "__main__":
#     demo()


# #case5 urlretrieve
# def progress(blk, blk_size, total_size):
#     print ("%d%d - %.02f%%" % (blk*blk_size, total_size,(float)(blk*blk_size)*100/total_size))
#
# def retrieve():
#     urllib.urlretrieve("https://www.douban.com", 'index.html', reporthook=progress)
#
# if __name__ == "__main__":
#     retrieve()

#case5 urlencode
def urlencode():
    params = {'score':100,"name":"爬虫",'comment':'very gppd'}
    qs = urllib.urlencode(params)
    print (qs)
    print (urlparse.parse_qs(qs))

def parse_qs():
    url = 'https://www.douban.com'
    result = urlparse.urlparse(url)
    params = urlparse.parse_qs(result.query)
    print (params)

if __name__ == "__main__":
    urlencode()
    parse_qs()



