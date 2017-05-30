# -*- coding: utf-8 -*-
import time
import datetime
import json
import requests
import os


class Tickets():

    def __init__(self):
        pass

    #获取车站代码
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

    # 分析列车信息页面
    def parse_data(self):

        # self.parse('BJP','SHH')
        self.trains=[]
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
            train['start_num']=data[16]
            train['arrive_num'] = data[17]
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
            train['seat_types']=data[34]

            self.trains.append(train)


    #获取余票信息
    def feach_num(self):
        pass

    #获取票价信息
    def feach_price(self):
        #https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?
        # train_no=240000G1010C
        # &from_station_no=01
        # &to_station_no=11
        # &seat_types=OM9
        # &train_date=2017-06-01

        trains = self.trains
        train_no=trains['train_no']
        start=trains['start_num']
        end=trains['arrive_num']
         seat_types=trains['seat_types']
        t = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")

        url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice"

        params = u"train_no=" + train_no + u"&from_station_no=" + start + u"&to_station_no=" + end + u"&seat_types=" + seat_types + u"&train_date=" + t
        try:
            s = requests.get(url, params=params.encode("utf-8"), verify=False)
        except Exception, e:
            print "fetch price fail. " + url
            raise e

        prices = json.loads(s.content)

        price = prices["data"]
        out = u"\n"
        if "A9" in price:
            out += price["A9"]
        else:
            out += u" --"
        if "P" in price:
            out += u" " + price["P"]
        else:
            out += u" --"
        if "M" in price:
            out += u" " + price["M"]
        else:
            out += u" --"
        if "O" in price:
            out += u" " + price["O"]
        else:
            out += u" --"
        if "A6" in price:
            out += u" " + price["A6"]
        else:
            out += u" --"
        if "A4" in price:
            out += u" " + price["A4"]
        else:
            out += u" --"
        if "A3" in price:
            out += u" " + price["A3"]
        else:
            out += u" --"
        if "A2" in price:
            out += u" " + price["A2"]
        else:
            out += u" --"
        if "A1" in price:
            out += u" " + price["A1"]
        else:
            out += u" --"
        if "WZ" in price:
            out += u" " + price["WZ"]
        else:
            out += u" --"
        if "MIN" in price:
            out += u" " + price["MIN"]
        else:
            out += u" --"

        self.price = out.encode("utf-8")


    def save(self):

        if not os.path.exists('train'):
            os.makedirs('train')
        with open('train/trains', 'w')as f:
            f.truncate()

            for train in self.trains:
                for i,j in train.items():
                    f.write(j)
                    f.write(self.price)

if __name__ == '__main__':
    tickets=Tickets()

    # tickets.stations_code()
    # tickets.parse_data()






