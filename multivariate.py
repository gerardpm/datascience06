# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:16:45 2015

@author: gerar_000
"""

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import math

loansData = pd.read_csv('C:\Users\\gerar_000\\Projects\\LoanStats3c.csv', skiprows=1)

print loansData['int_rate'][0:5]
print loansData['mths_since_last_delinq'][0:5]
print loansData['revol_bal'][0:5]


loansData['Interest.Rate'] = loansData['int_rate'].apply(lambda x: str(x).rstrip('%'))
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)

def fix_digits(x):
 if math.isnan(x):
 	return 999999.0
 else:
 	return x

loansData['Loan.Length'] = loansData['revol_bal'].apply(fix_digits)

loansData['FICO.Score'] = loansData['revol_bal']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()

FICO = []

for j in range(len(A)):
    B = A[j].split("-")
    C = float(B[0])   
    FICO.append(C)          

loansData['FICO.Score'] = FICO

intrate = loansData['Interest.Rate']
intrate[np.isnan(intrate)] = 0
loanamt = loansData['out_prncp_inv']
loanamt[np.isnan(loanamt)] = 0
fico = loansData['FICO.Score']
fico[np.isnan(fico)] = 0
monthly_income = loansData['annual_inc']
monthly_income[np.isnan(monthly_income)] = 0


house_ownership = loansData['home_ownership']
house_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in house_ownership]

y = np.matrix(intrate).transpose()


x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x3 = np.matrix(monthly_income).transpose()
x4 = np.matrix(house_ownership).transpose()
# New variables are added to the regression, similar to linear regression

x = np.column_stack([x1,x2,x3, x4])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:4]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared