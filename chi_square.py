
# coding: utf-8

# In[3]:

from scipy import stats


# In[4]:

import pandas as pd


# In[5]:

import collections


# In[6]:

import matplotlib.pyplot as plt


# In[7]:

loansData = loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[8]:

loansData.dropna(inplace=True)


# In[9]:

freq = collections.Counter(loansData['Open.CREDIT.Lines'])


# In[ ]:

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()


# In[ ]:

chi, p = stats.chisquare(freq.values())


# In[ ]:



