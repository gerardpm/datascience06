
# coding: utf-8

# In[15]:

from scipy import stats


# In[16]:

import pandas as pd


# In[17]:

import collections


# In[22]:

import matplotlib.pyplot as plt


# In[18]:

loansData = loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[19]:

loansData.dropna(inplace=True)


# In[7]:

freq = collections.Counter(loansData['Open.CREDIT.Lines'])


# In[23]:

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()


# In[31]:

chi, p = stats.chisquare(freq.values())


# In[32]:

chi


# In[33]:

p


# In[ ]:



