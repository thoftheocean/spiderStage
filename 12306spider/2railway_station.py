#coding:utf-8

#获取所有铁路局客运站数据
import time
import requests
from bs4 import BeautifulSoup
import os


def fetch_data(url,railway_adm_name,desc,f):

    #获取客运站链接是一个相对地址，转化为绝对地址。如：./nanchang/201001/t20100124_1181.html
    url = 'http://www.12306.cn/mormhweb/kyyyz/'+url[1:]

    try:
        req = requests.get(url)
    except Exception,e:
        print 'requests url fail'+url
        print e
        return

    soup = BeautifulSoup(req.content, 'lxml')
    datas = soup.select('table table tr ')

    if len(datas) <= 2:
        req = 'find nothing'+url+''+railway_adm_name.encode('utf-8')+''+desc.encode('utf-8')
        print req
        f.write(req+'\n')

#找出tr中td里面的内容加上铁路局加上车站/乘降所
    for i in range(0, len(datas)):
        if i < 2:
            continue
        infos = datas[i].find_all('td')

        out = u''
        for info in infos:
            out += info.text
            out += u'\t '

        out += railway_adm_name+u'\t'+desc
        s = out.encode('utf-8')
        f.write(s+'\n')
        print s

if __name__ == '__main__':

    url = 'http://www.12306.cn/mormhweb/kyyyz/'

    try:
        req = requests.get(url)
    except Exception, e:
        print 'requests url fail'+url
        print e

    soup = BeautifulSoup(req.content, 'lxml')
    names = soup.select('#secTable > tbody > tr > td')
    sub_urls = soup.select('#mainTable td.submenu_bg > a')#注意之间的间隔

    if not os.path.exists('railway_info'):
        os.makedirs('railway_info')

    with open('railway_info/railway_station.txt','w') as f:
        for i in range(0,len(names)):

            sub_urls1 = sub_urls[i * 2]['href']
            print sub_urls1
            fetch_data(sub_urls1,names[i].text, u'车站',f)
            time.sleep(5)

            sub_urls2 = sub_urls[i * 2 + 1]['href']
            print sub_urls2
            fetch_data(sub_urls2, names[i].text, u'乘降所',f)
            time.sleep(5)#休眠5ms
