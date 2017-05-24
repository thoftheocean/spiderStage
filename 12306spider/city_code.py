# -*- coding: utf-8 -*-

import time
import datetime
import json

import requests
import os

def fetch_stations(f):
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006"

    try:
        s = requests.get(url, verify=False)
    except Exception, e:
        print "fetch stations fail. " + url
        raise e

    station_str = s.content.decode("utf-8")
    
    stations = station_str.split(u"@")

    for i in range(1, len(stations)):
        station = stations[i].split(u"|")
        out = station[1] + u" " + station[2] + u"\n"
        f.write(out.encode("utf-8"))
        #fd.write("\n")
        #print s

if __name__ == "__main__":

    if not os.path.exists('railway_info'):
        os.makedirs('railway_info')
    with open("railway_info/city_code.txt", "w") as f:
        fetch_stations(f)
        





    



    


    














# vim: set ts=4 sw=4 sts=4 tw=100 et:
