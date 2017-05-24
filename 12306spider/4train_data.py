# -*- coding: utf-8 -*-
#描述：票价查询网址https://kyfw.12306.cn/otn/leftTicketPrice/init
#分析：北京到上海
#车站北京到上海： https://kyfw.12306.cn/otn/leftTicketPrice/query?leftTicketDTO.train_date=2017-05-22&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&leftTicketDTO.ticket_type=1&randCode=K6eu
#车次D321：https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=240000D3210C&from_station_telecode=VNP&to_station_telecode=SHH&depart_date=2017-05-22
#票价：https://kyfw.12306.cn/otn/leftTicketPrice/queryPublicPrice?train_no=240000D3210C&train_code=D321&from_station_telecode=VNP&to_station_telecode=SHH&seat_types=&train_date=2017-05-22

import time
import datetime
import json
import requests

#车站https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=760000K29207&from_station_telecode=CDW&to_station_telecode=SHH&depart_date=2017-05-22


#获取车站的代码
def fetch_stations(train_no,start, end, t, fd):
    #https://kyfw.12306.cn/otn/czxx/queryByTrainNo?
    # train_no=240000D3210C
    # &from_station_telecode=VNP
    # &to_station_telecode=SHH
    # &depart_date=2017-05-22
    url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo"

    params = u"train_no=" + train_no + u"&from_station_telecode=" + start + u"&to_station_telecode=" + end + "&depart_date=" + t

    try:
        s = requests.get(url, params = params.encode("utf-8"), verify = False)
    except Exception, e:
        print "fetch stations fail. " + url
        raise e

    stations = json.loads(s.content)

    for station in stations["data"]["data"]:
        out = u""
        out += station["station_no"]
        out += u" " + station["station_name"]
        out += u" " + station["arrive_time"]
        out += u" " + station["start_time"]
        out += u" " + station["stopover_time"]

        s = out.encode("utf-8")
        fd.write("\n")
        fd.write(s)
        print s
    fd.write("\n")

def fetch_price(train_no,train_code,start, end,seat_types,f, fd):
    #https://kyfw.12306.cn/otn/leftTicketPrice/queryPublicPrice?
    # train_no=240000D3210C
    # &train_code=D321
    # &from_station_telecode=VNP
    # &to_station_telecode=SHH
    # &seat_types=
    # &train_date=2017-05-22
    url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice"

    params = u"train_no=" + train_no +u"train_code"+train_code + u"&from_station_no=" + start + u"&to_station_no=" + end + u"&seat_types=" + seat_types + u"&train_date=" + t
    try:
        s = requests.get(url, params = params.encode("utf-8"), verify = False)
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

    s = out.encode("utf-8")
    fd.write(s)
    fd.write("\n")
    print s

#获取路线信息
def fetch_data(t, start, end,fd):
    #https://kyfw.12306.cn/otn/leftTicketPrice/query?
    # leftTicketDTO.train_date=2017-05-22
    # &leftTicketDTO.from_station=BJP
    # &leftTicketDTO.to_station=SHH
    # &leftTicketDTO.ticket_type=1
    # &randCode=K6eu
    url = "https://kyfw.12306.cn/otn/leftTicketPrice/query"

    # 获取12306票价查询验证码
    # url1 = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=other&rand=sjrand'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    # req = requests.get(url=url1, headers=headers, verify=False)
    # with open('img/code.jpg', 'wb') as f:
    #     f.write(req.content)
    # code=raw_input('验证码：')
    # # print req.cookies
    # str=req.cookies['JSESSIONID']
    # cookies={'JSESSIONID':str}
    # print cookies
    # # print code

    #正则表达式获取验证码
    url = 'https://kyfw.12306.cn/otn/leftTicketPrice/init'
    req = requests.get(url,verify=False)
    pattern = '<img src="(.*?)" onclick'
    import re
    pattern1 = re.compile(pattern,re.S)
    items = re.findall(pattern1, req.content)

    # print req.cookies['jsessionid']




    #
    # f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
    # cookies = {}  # 初始化cookies字典变量
    # for line in f.read().split(';'):  # 按照字符：进行划分读取
    #     # 其设置为1就会把字符串拆分成2份
    #     name, value = line.strip().split('=', 1)
    #     cookies[name] = value  # 为字典cookies添加内容

    data={'randCode':code,'rand':'sjrand','_json_att':''}
    print data

    s=requests.post('https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn',data=data,cookies=cookies,verify=False)

    # print s.url,1
    print s.content,2
    print s.cookies,3

    params = u"leftTicketDTO.train_date" + t + u"leftTicketDTO.from_station=" + start + u"&leftTicketDTO.to_station" +end+u'leftTicketDTO.ticket_type=1'+u'&randCode='+code
    try:
        s = requests.get(url, params = params.encode("utf-8"), verify = False)
    except Exception, e:
        print "requests url fail.", url
        return

    print s.content

    datas = json.loads(s.content)

    if "datas" not in datas["data"]:
        print "no train", t, start.encode("utf-8"), end.encode("utf-8")
        return

    for data in datas["data"]["queryLeftNewDTO"]:

        out = u"--------------------------------------\n"
        out += data["from_station_name"]
        out += u" " + data["end_station_name"]
        out += u" " + data["station_train_code"]
        out += u"\n" + data["swz_num"]
        out += u" " + data["tz_num"]
        out += u" " + data["zy_num"]
        out += u" " + data["ze_num"]
        out += u" " + data["gr_num"]
        out += u" " + data["rw_num"]
        out += u" " + data["yw_num"]
        out += u" " + data["rz_num"]
        out += u" " + data["yz_num"]
        out += u" " + data["wz_num"]
        out += u" " + data["qt_num"]

        s = out.encode("utf-8")
        fd.write(s)
        fd.write("\n")
        print s

        time.sleep(2)
        fetch_price(data["train_no"],data["station_train_code"],data["from_station_no"], data["to_station_no"], data["seat_types"],t, fd)

        time.sleep(2)
        fetch_stations(t, start, end, data["train_no"], fd)

        time.sleep(2)

if __name__ == "__main__":

    with open("13.txt", "w") as fd:
        fetch_data((datetime.datetime.now() + datetime.timedelta(days = 3)).strftime("%Y-%m-%d"), "BJP", "SHH", fd)



















