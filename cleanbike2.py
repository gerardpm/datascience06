# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 16:03:19 2015

@author: gerar_000
"""
import matplotlib.pyplot as plt
import pandas as pd
import requests
import time
import collections

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

from dateutil.parser import parse 

exec_time = parse(r.json()['executionTime'])
with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

id_bikes = collections.defaultdict(int)
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
        con.commit()

time.sleep(60)

con.close()


con = lite.connect('citi_bike2.db')
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')

hour_change = collections.defaultdict(int)
for col in df.columns:
    station_vals = df[col].tolist()
    station_id = col[1:]
    station_change = 0
    for k,v in enumerate(station_vals):
        if k < len(station_vals) - 1:
            station_change += abs(station_vals[k] - station_vals[k+1])
    hour_change[int(station_id)] = station_change 
    
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())

    return k[v.index(max(v))]

max_station = keywithmaxval(hour_change)

cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data = cur.fetchone()

print "The most active station is station id %s at %s latitude: %s longitude: %s " % data

print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')

import matplotlib.pyplot as plt

plt.bar(hour_change.keys(), hour_change.values())
plt.show()