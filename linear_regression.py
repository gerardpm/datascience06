
# coding: utf-8

# In[22]:

import pandas as pd


# In[23]:

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[24]:

loansData['Interest.Rate'][0:5]


# In[25]:

loansData['Loan.Length'][0:5]


# In[26]:

loansData['FICO.Range'][0:5]


# In[27]:

def f(x):
    '''This function takes x as a parameter and returns x squared'''
    print x**2


# In[28]:

f(2)


# In[29]:

g = lambda x: x**2


# In[30]:

g(2)


# In[41]:

import numpy as np


# In[42]:

import matplotlib.pyplot as plt


# In[43]:

plt.figure()


# In[44]:

p = loansData['FICO.Score'].hist()


# In[ ]:



