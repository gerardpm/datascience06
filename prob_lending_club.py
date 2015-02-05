
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[2]:

import pandas as pd


# In[3]:

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[4]:

loansData.dropna(inplace=True)


# In[5]:

loansData.boxplot(column='Amount.Requested')


# In[6]:

plt.show()


# In[7]:

import scipy.stats as stats


# In[8]:

plt.figure()


# In[9]:

graph = stats.probplot(loansData['Amount.Requested'],dist="norm", plot=plt)


# In[ ]:

plt.show()


# In[ ]:

#There is a minimal difference (.001) in the amount funded by investors vs. amount requested. This may signal that there may be a strong correlation between requester and funder.

