
#coding:utf-8

#获取所有铁路局的信息
import requests
from bs4 import BeautifulSoup
import pymysql.cursors

class RailWay():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='151932',
                               db='train',
                               charset='utf8')

        self.c = self.conn.cursor()
        self.c.execute('''
                        DROP TABLE IF EXISTS bureaus;
                        create table if not exists bureaus(
                        id TINYINT UNSIGNED AUTO_INCREMENT KEY,
                        province VARCHAR(50)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8;
                        ''')

    def railway(self):

        url = 'http://www.12306.cn/mormhweb/kyyyz/'

        try:
            req = requests.get(url)
        except Exception, e:
            print 'requests url fail'+url
            print e

        soup = BeautifulSoup(req.content, 'lxml')
        results = soup.select('#secTable > tbody > tr > td ')
        for result in results:
            print result.text
            self.c.execute('insert ignore into bureaus  set province=%s',result.text)
            self.conn.commit()

if __name__ == '__main__':
    railway = RailWay()
    railway.railway()