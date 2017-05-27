#-*-coding:UTF-8-*-

#获取所有铁路局客运站数据
import pymysql
import time
import requests
from bs4 import BeautifulSoup
import os

class Stations():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='151932',
                                    db='train',
                                    charset='utf8')

        self.c = self.conn.cursor()
        self.c.execute('''
                       drop table if exists `stations`;
                       create table `stations` (
                                        bureau varchar(10) not null,
                                        station varchar(15) not null,
                                        name varchar(15) not null,
                                        address varchar(50) not null,
                                        passenger varchar(10) not null,
                                        luggage varchar(10) not null,
                                        package varchar(10) not null,
                                        primary key(bureau, station, name)
                                      ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                        ''')

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
    def fetch_stations(self,url1):

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


    def save(self,bureaus_name,desc):

    # #找出tr中td里面的内容加上铁路局加上车站/乘降所
        for i in range(0,len(self.datas)):
            if i<2:
                continue
            infos=self.datas[i].find_all('td')

            item=dict()
            item['bureau']=bureaus_name
            item['station']=desc
            item["name"] = infos[0].text
            item["address"] = infos[1].text
            item["passenger"] = infos[2].text.strip()
            item["luggage"] = infos[3].text.strip()
            item["package"] = infos[4].text.strip()

            self.sql = "INSERT IGNORE INTO `stations` (`bureau`, `station`,\
                `name`, `address`, `passenger`, `luggage`,\
                `package`) VALUES\
                (%s, %s, %s, %s, %s, %s, %s)"

            self.c.execute(self.sql, (item["bureau"], item["station"],
                                           item["name"], item["address"],
                                           item["passenger"], item["luggage"],
                                           item["package"]))
            self.conn.commit()

            #从数据库中获取内容
            self.c.execute("SELECT *FROM stations")
            # print self.c.fetchall()
            for inf in self.c.fetchall():
                dict1 = dict()
                dict1['bureau'] = inf[0]
                dict1['station'] = inf[1]
                dict1["name"] = inf[2]
                dict1["address"] = inf[3]
                dict1["passenger"] = inf[4]
                dict1["luggage"] = inf[5]
                dict1["package"] = inf[6]
                print dict1
                # print "%s %s" % (inf[2], inf[3])


    def run(self):
        self.feach_bureaus()

        for i in range(0, len(self.names)):
            sub_urls1 = self.sub_urls[i * 2]['href']
            self.fetch_stations(sub_urls1)
            self.save(self.names[i].text, '车站')
            time.sleep(1)

            sub_urls2 = self.sub_urls[i * 2 + 1]['href']
            self.fetch_stations(sub_urls2)
            self.save(self.names[i].text, '乘降所')
            time.sleep(1)  # 休眠5ms


if __name__ == '__main__':

    stations = Stations()
    stations.run()


