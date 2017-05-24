# -*- coding: utf-8 -*-

#查询成都k291的正晚点信息

import time
import datetime
import json

import urllib
import requests

def fetch_schedule(train_code,station_name,depart):

    #http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/cx.jsp?
    # cz=%B3%C9%B6%BC
    # &cc=k291
    # &cxlx=0
    # &rq=2017-05-19
    # &czEn=-E6-88-90-E9-83-BD
    # &tp=1495184632260

    url='http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/cx.jsp'

    params={'cz':station_name,
            'cc':train_code,
            "rq": datetime.datetime.now().strftime("%Y-%m-%d"),
            'cxlx':'1'if depart else'0',
            'czEn':urllib.quote(station_name.encode('utf-8')).replace('%','-'),
            'tp':int(time.time()*1000)}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    try:
        req=requests.get(url,params=params,headers=headers)
    except Exception,e:
        print 'request fail'+url
        raise e
    print req.content.strip().decode('gbk').encode('utf-8')
    # print req.content


if __name__ == '__main__':
    fetch_schedule('k291', u'成都' ,False)