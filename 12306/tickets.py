# -*- coding: utf-8 -*-
import time
import datetime
import json
import urllib
import requests


class Tickets():

    def __init__(self):
        pass

    def stations_code(self):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006"

        try:
            s = requests.get(url, verify=False)
        except Exception, e:
            print "fetch stations fail. " + url
            raise e

        station_str = s.content.decode("utf-8")
        stations = station_str.split(u"@")

        code = dict()
        stationcode=[]
        for i in range(1, len(stations)):
            station = stations[i].split(u"|")
            code['station']=station[1]
            code['code']=station[2]
            stationcode.append(code)
        # print stationcode

    def parse(self,start,end):

        #https://kyfw.12306.cn/otn/leftTicket/query?
        # leftTicketDTO.train_date=2017-06-01
        # &leftTicketDTO.from_station=BJP
        # &leftTicketDTO.to_station=SHH
        # &purpose_codes=ADULT

        url='https://kyfw.12306.cn/otn/leftTicket/query?'
        t = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        print type(t)
        print start
        params = "leftTicketDTO.train_date=" + t + "&leftTicketDTO.from_station=" + start + "&leftTicketDTO.to_station=" + end + '&purpose_codes=ADULT'
        #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-06-01&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
        try:
            req = requests.get(url+params, verify=False)
        except Exception, e:
            print "requests url fail.", url
            print e
            return
        self.datas = json.loads(req.content)


    def parse_data(self):

        self.parse('BJP','SHH')
        trains=[]
        train=dict()
        for data in self.datas['data']['result']:
            data=data.split('|')
            train['train_no']=data[2]
            train['code'] = data[3]
            train['start_station'] = data[4]
            train['end_station'] = data[5]
            train['start_time']=data[8]
            train['arrive_time'] = data[9]
            train['long_time'] = data[10]
            train['start_date'] = data[13]
            train['tz_num']=data[25]
            train['zy_num']=data[31]
            train['ze_num']=data[30]
            train['swz_num']=data[32]
            train['gr_num']=data[21]
            train['rw_num']=data[22]
            train['yw_num']=data[29]
            train['yz_num']=data[28]
            train['rz_num']=data[24]
            train['wz_num']=data[26]
            trains.append(train)
        print trains

    def feach_num(self):

    def feach_price(self):

        pass

    def save(self, bureaus_name, desc, f):
        # #找出tr中td里面的内容加上铁路局加上车站/乘降所
        for i in range(0, len(self.datas)):
            if i < 2:
                continue
            infos = self.datas[i].find_all('td')

            out = bureaus_name.encode('utf-8') + '\t' + desc + '\t'

            for info in infos:
                out += info.text.encode('utf-8') + '  '
            f.write(out + '\n')
            print out


if __name__ == '__main__':
    tickets=Tickets()

    # tickets.stations_code()
    tickets.parse_data()






