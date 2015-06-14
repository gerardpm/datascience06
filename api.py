# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 14:04:07 2015

@author: gerar_000
"""

import pandas as pd
import requests
import time
import datetime

cities = { "Atlanta": '33.762909,-84.422675',
           "Boston": '42.331960,-71.020173',
           "Chicago": '41.837551,-87.681844',
           "Denver": '39.761850,-104.881105',
           "Las Vegas": '36.229214,-115.26008',
           "Los Angeles": '34.019394,-118.410825',
           "Miami": 'FL,25.775163,-80.208615'
        }

for city in cities.keys():
    llstr = cities[city]
    lllist = llstr.split(',')
    lat = lllist[0]
    lon = lllist[1]
    
apikey = '1dc64ea7cfd540026a8359868cf035f4'
lat = lllist[0]
lon = lllist[1]
    
time = datetime.datetime.now() - datetime.timedelta(days=30)
start_date = datetime.datetime.now() - datetime.timedelta(days=30)
utime = start_date.strftime('%H:%M:%S')
rurl = 'https://api.forecast.io/forecast/' + apikey + '/' + lat + ',' + lon + ',' + utime
print(rurl)

r = requests.get(rurl)
r.text
r.json().keys()
(r.json()['code'])




