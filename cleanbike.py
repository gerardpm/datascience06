# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 16:03:19 2015

@author: gerar_000
"""

import requests
r = requests.get('http://www.citibikenyc.com/stations/json')
r.text
r.json()
r.json().keys()
r.json()['executionTime']
r.json()['stationBeanList']
(r.json()['stationBeanList'])

key_list = [] 
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

r.json()['stationBeanList'][0]

from pandas.io.json import json_normalize
df = json_normalize(r.json()['stationBeanList'])

import matplotlib.pyplot as plt
import pandas as pd

df['availableBikes'].hist()
plt.show()

df['totalDocks'].hist()
plt.show()

df['testStation'].hist()
plt.show()

df['totalDocks'].mean()

condition = (df['statusValue'] == 'In Service')
df[condition]['totalDocks'].mean()

df['totalDocks'].median()
df[df['statusValue'] == 'In Service']['totalDocks'].median()

import sqlite3 as lite

con = lite.connect('citi_bike2.db')
cur = con.cursor()
with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')
    
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

with con:
    for station in r.json()['stationBeanList']:
               cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
station_ids = df['id'].tolist()
station_ids = ['_' + str(x) + ' INT' for x in (station_ids)]

station_ids
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

import time

from dateutil.parser import parse 

import collections

exec_time = parse(r.json()['executionTime'])
with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s')),)

id_bikes = collections.defaultdict(int)
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']
with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
        con.commit()

time.sleep(60)

con.close()