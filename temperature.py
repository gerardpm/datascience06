# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 14:04:07 2015

@author: gerar_000
"""

import pandas as pd
import requests
import time
import datetime
import sqlite3 as lite

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
end_date = datetime.datetime.now()
utime = start_date.strftime('%H:%M:%S')
rurl = 'https://api.forecast.io/forecast/' + apikey + '/' + lat + ',' + lon + ',' + utime
print(rurl)

con = lite.connect('weather.db')
cur = con.cursor()
cities.keys()
with con:
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, "Atlanta" REAL, "Boston" REAL, "Chicago" REAL, "Denver" REAL, "Las Vegas" REAL, "Los Angeles" REAL, "Miami" REAL);')

query_date = end_date - datetime.timedelta(days=30) 

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) 
    while query_date < end_date:
        r = requests.get(rurl + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))
        #
        with con:
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))
            #
            query_date += datetime.timedelta(days=1) 

con.close()

import os
os.getcwd()

