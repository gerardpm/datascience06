# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 18:50:33 2015

@author: gerar_000
"""

import pandas as pd
import numpy as np
import statsmodels.api as stats
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()

FICO = []

for j in range(len(A)):
    B = A[j].split("-")
    C = float(B[0])   
    FICO.append(C)          

loansData['FICO.Score'] = FICO

loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)  
plt.figure()

loansData['FICO.Score'].hist()
plt.show()