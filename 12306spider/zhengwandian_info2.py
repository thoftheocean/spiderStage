# -*- coding: utf-8 -*-

#描述：获取所有车次的正晚点信息

import time
import datetime
import json

import urllib
import requests

def load_resource():
    arrives={}
    for i in range(0,24):
        arrives[i]=[]
    with open('train_info.txt','r')as f:
        new_train_line =0
        code=''
        for line in f.xreadlines():
            new_train_line+=1
            if line.startswith('-'):
                new_train_line=0;
            elif new_train_line==1:
                code=line[:line.find('(')]
            elif line=='\n':
                continue
            else:
                params=line.split('')
                name=params[1]
                arrive=params[2]
                if not arrive.startswith('-'):
                    t=datetime.datetime.strptime(arrive,'%H.%M')
                    arrives[t.hour].append((code,name))

        return arrives
def fetch_schedule(train_code, station_name, depart):

    url = 'http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/cx.jsp'

    params = {'cz': station_name,
              'cc': train_code,
              "rq": datetime.datetime.now().strftime("%Y-%m-%d"),
              'cxlx': '1' if depart else'0',
              'czEn': urllib.quote(station_name.encode('utf-8')).replace('%', '-'),
              'tp': int(time.time() * 1000)}

    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}

    try:
        s = requests.get(url, params = params, headers = headers)
    except Exception, e:
        print "request fail. " + url
        raise e

    return s.content.strip().decode("gbk")

if __name__ == "__main__":
    arrives = load_resource()

    while True:
        t = datetime.datetime.now()
        # 这样循环有什么问题没？
        curs = arrives[(t.hour + 2) % 24]
        for cur in curs:
            time.sleep(2)
            result = fetch_schedule(cur[0], cur[1], 0)
            # 判断返回字符串是否包含结果
            if result.startswith(u"预计"):
                print result.encode("utf-8")

