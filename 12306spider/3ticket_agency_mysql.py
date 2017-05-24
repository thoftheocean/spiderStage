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

    j = json.loads(s.content)
    return j["data"]

def fetch_data(url, province, cursor):
    sql = "INSERT IGNORE INTO ticket_agency (`province`, `city`, `county`,\
            `address`, `name`, `windows`, `start`, `end`) VALUES\
            (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        s = requests.get(url, params = {"province":province, "city":"", "county":""}, verify = False)
    except Exception, e:
        print "requests url fail.", url, province.encode("utf-8")
        return

    datas = json.loads(s.content)

    for data in datas["data"]["datas"]:
        cursor.execute(sql, (data["province"], data["city"],
                            data["county"], data["address"],
                            data["agency_name"], data["windows_quantity"],
                            data["start_time_am"] + u"00",
                            data["stop_time_pm"] + u"00"))

if __name__ == "__main__":
    provs = fetch_provinces()

    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"

    conn = pymysql.connect(host = 'localhost', port = 3306,
                                user = 'root',
                                password = '151932',
                                db = 'train12306',
                                charset = 'utf8')
    with conn.cursor() as cursor:
        for prov in provs:
            fetch_data(url, prov["chineseName"], cursor)
            conn.commit()#提交数据，保证数据写入数据库中
            time.sleep(5)




