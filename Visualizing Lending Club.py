
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

import matplotlib.pyplot as plt


# In[6]:

import pandas as pd


# In[7]:

loansData.boxplot(column='Amount.Funded.By.Investors')


# In[8]:

plt.show()


# In[9]:

loansData.hist(column='Amount.Funded.By.Investors')


# In[11]:

plt.show()


# In[12]:

import scipy.stats as stats


# In[13]:

plt.figure()


# In[18]:

graph = stats.probplot(loansData['Amount.Funded.By.Investors'],dist="norm", plot=plt)


# In[19]:

plt.show()


# In[ ]:



