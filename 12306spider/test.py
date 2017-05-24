#coding:utf-8

# import requests
#
# #请求方法为get方法
#
# rg = requests.get('https://www.baidu.com')
#
# #打印出请求的方法
# print rg.request.method
#
# #打印出请求的路径
# print rg.request.path_url
#
# #打印出请求的头
# rh = rg.request.headers
# for k, c in rh.items():
#     print k, ':', c
#
# #打印请求体（get方法一般为空）
# print rg.request.body
#
# #打印返回状态码
# print rg.status_code
# print rg.ok
#
# #打印返回的网页源代码（解码后的消息
# print rg.text
# #打印返回的网页源代码（未解码的消息）
# print rg.content
# with open('1.html','w') as f:
#     f.write(rg.content)
#
#
# # #请求方法为get方法
# # #本网址是一个错误的post，所以会被重定向。返回的是上一个网址的信息。所以添加禁止重定向
# # rp = requests.post('https://www.baidu.com/s?wd=hao123', allow_redirects=False)
# #
# # #打印出请求的方法
# # print rp.request.method
# #
# # headers = {}
#
# import json
import requests

f=open(r'test.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
print cookies