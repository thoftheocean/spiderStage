#-*-coding:UTF-8-*-

#获取所有铁路局客运站数据
import time
import requests
from bs4 import BeautifulSoup
import os

class Stations():
    def __init__(self):

        self.names=''
        self.sub_urls=''
    #获取第一个页面的信息
    def feach_bureaus(self):
        url = 'http://www.12306.cn/mormhweb/kyyyz/'

        try:
            req = requests.get(url)
        except Exception, e:
            print 'requests url fail' + url
            print e

        soup = BeautifulSoup(req.content, 'lxml')
        #获取铁路局
        self.names = soup.select('#secTable > tbody > tr > td')
        #获取铁路局下站点
        self.sub_urls = soup.select('#mainTable td.submenu_bg > a')  # 注意之间的间隔

    #获取站点信息
    def fetch_stations(self,url1,bureaus_name,desc,f):

        #获取客运站链接是一个相对地址，转化为绝对地址。如：./nanchang/201001/t20100124_1181.html
        url = 'http://www.12306.cn/mormhweb/kyyyz/'+url1[1:]
        try:
            req = requests.get(url)
        except Exception,e:
            print 'requests url fail'+url
            print e
            return
        soup = BeautifulSoup(req.content, 'lxml')
        self.datas = soup.select('table table tr ')

        if len(self.datas) <= 2:
            req = 'find nothing'+url+''+bureaus_name.encode('utf-8')+''+desc.encode('utf-8')
            f.write(req+'\n')

    def save(self,bureaus_name,desc,f):
    # #找出tr中td里面的内容加上铁路局加上车站/乘降所
        for i in range(0,len(self.datas)):
            if i<2:
                continue
            infos=self.datas[i].find_all('td')

            out=bureaus_name.encode('utf-8')+'\t'+desc+'\t'

            for info in infos:
                out += info.text.encode('utf-8')+'  '
            f.write(out+'\n')
            print out


    def run(self):

        self.feach_bureaus()

        if not os.path.exists('train'):
            os.makedirs('train')

        with open('train/stations.txt', 'w') as f:
            f.truncate()
            for i in range(0, len(self.names)):

                sub_urls1 = self.sub_urls[i * 2]['href']
                self.fetch_stations(sub_urls1,self.names[i].text, '车站', f)
                self.save(self.names[i].text, '车站', f)
                time.sleep(1)

                sub_urls2 = self.sub_urls[i * 2 + 1]['href']
                self.fetch_stations(sub_urls2,self.names[i].text, '乘降所', f)
                self.save(self.names[i].text, '乘降所', f)
                time.sleep(1)  # 休眠5ms


if __name__ == '__main__':

    stations = Stations()
    stations.run()


