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

def fetch_data(province):
    # https://kyfw.12306.cn/otn/queryAgencySellTicket/query?province=%E5%AE%89%E5%BE%BD&city=&county=
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"
    try:
        req=requests.get(url,params={'province':province,'city':'','county':''},verify=False)#params查询参数

    except Exception, e:
        print 'requests url fail.',url,province.encode('utf-8')
        print e
        return

    datas = json.loads(req.content)
    return datas

def save(datas):

    if not os.path.exists('train'):
        os.makedirs('train')

    with open('train/angencys.txt', 'w')as f:
        f.truncate()
        for data in datas['data']['datas']:
            out = u''
            out +=data['province']+data['city']+data['county']+data['agency_name']+data['address']+data['windows_quantity']
            start = data['start_time_am']
            end = data['stop_time_pm']
            out += u' '+start[:2]+u':'+start[2:]+'-'+end[:2]+u':'+end[2:]
            f.write(out.encode('utf-8')+'\n')
            print out

if __name__ == '__main__':
    provs = fetch_provinces()
    for prov in provs['data']:
        datas=fetch_data(prov['chineseName'])
        save(datas)
        time.sleep(5)



