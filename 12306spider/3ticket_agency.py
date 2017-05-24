# usr/bin/env python
# encoding:utf-8
# author hexi

import time
import json
import requests
import os

def fetch_provinces():

    #获取所有省份名称
    url='https://kyfw.12306.cn/otn/userCommon/allProvince'

    try:
        req = requests.get(url,verify=False) #verify=False 不进行验证
    except Exception,e:
        print 'fetch province fail.'+url
        raise e

    provs = json.loads(req.content)
    return provs

def fetch_data(url,province,f):

    try:
        req=requests.get(url,params={'province':province,'city':'','county':''},verify=False)#params查询参数

    except Exception, e:
        print 'requests url fail.',url,province.encode('utf-8')
        print e
        return

    datas= json.loads(req.content)

    for data in datas['data']['datas']:

        out = u''
        out += data['province']+data['city']+data['county']+data['agency_name']+data['address']+data['windows_quantity']
        start = data['start_time_am']
        end = data['stop_time_pm']
        out += u' '+start[:2]+u':'+start[2:]+u'-'+end[:2]+u':'+end[2:]

        s = out.encode('utf-8')
        f.write(s+'\n')
        print s


if __name__ == '__main__':
    provs = fetch_provinces()
    #https://kyfw.12306.cn/otn/queryAgencySellTicket/query?province=%E5%AE%89%E5%BE%BD&city=&county=
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"

    if not os.path.exists('railway_info'):
        os.makedirs('railway_info')

    with open('railway_info/ticket_agent.txt', 'w')as f:
        for prov in provs['data']:
            fetch_data(url, prov['chineseName'], f)
            time.sleep(5)



