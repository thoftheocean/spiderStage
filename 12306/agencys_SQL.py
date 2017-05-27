# -*- coding: utf-8 -*-

import time
import json
import requests
import pymysql.cursors

def fetch_provinces():
    url = "https://kyfw.12306.cn/otn/userCommon/allProvince"

    try:
        s = requests.get(url, verify = False)
    except Exception, e:
        print "fetch provinces. " + url
        raise e

    provs = json.loads(s.content)["data"]
    return provs

def fetch_data(province):
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"

    try:
        s = requests.get(url, params = {"province":province, "city":"", "county":""}, verify = False)
    except Exception, e:
        print "requests url fail.", url, province.encode("utf-8")
        return
    datas = json.loads(s.content)
    return datas


def save(datas):

    conn = pymysql.connect(host='localhost', port=3306,
                           user='root',
                           password='151932',
                           db='train',
                           charset='utf8')
    c= conn.cursor()
    c.execute('''
                drop table if exists `agencys`;
                create table `agencys` (
                `province` varchar(10) not null,
                `city` varchar(15) not null,
                `county` varchar(15) not null,
                `address` varchar(50) primary key,
                `name` varchar(50) not null,
                `windows` int,
                `start` time,
                `end` time) ENGINE=InnoDB DEFAULT CHARSET=utf8;

                ''')
    sql = "INSERT IGNORE INTO ticket_agency (`province`, `city`, `county`,\
        `address`, `name`, `windows`, `start`, `end`) VALUES\
        (%s, %s, %s, %s, %s, %s, %s, %s)"

    for data in datas["data"]["datas"]:
        c.execute(sql, (data["province"], data["city"],
                             data["county"], data["address"],
                             data["agency_name"], data["windows_quantity"],
                             data["start_time_am"] + u"00",
                             data["stop_time_pm"] + u"00"))
    conn.commit()


if __name__ == "__main__":
    provs = fetch_provinces()
    for prov in provs:
        datas=fetch_data(prov["chineseName"])
        save(datas)
        time.sleep(5)

