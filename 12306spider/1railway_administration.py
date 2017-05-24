#coding:utf-8

#获取所有铁路局的信息
import requests
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':

    url = 'http://www.12306.cn/mormhweb/kyyyz/'

    try:
        req = requests.get(url)
    except Exception, e:
        print 'requests url fail'+url
        print e

    soup = BeautifulSoup(req.content, 'lxml')
    results = soup.select('#secTable > tbody > tr > td')

    if not os.path.exists('railway_info'):
        os.makedirs('railway_info')

    with open('railway_info/railway_administration','w') as f:

        for result in results:
            f.write(result.text.encode('utf-8')+'\n')
            print result.text