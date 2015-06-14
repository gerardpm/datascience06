# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:08:56 2015

@author: gerar_000
"""

from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
import pandas as pd


url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content) 
A = soup('table')[6].findAll('tr', {'class': 'tcont'})
B = [x for x in A if len(x)== 25] 

records = []
for rows in B:
    col = rows.findAll('td')
    country = col[0].string
    year = col[1].string
    total = col[4].string
    men = col[7].string
    women = col[10].string
    record = (country, year, total, men, women)
    records.append(record)
column_name = ['country', 'year', 'total', 'men', 'women']
table = pd.DataFrame(records, columns = column_name )
table.to_csv('C:\Users\gerar_000\Projects' , index = t)
    


