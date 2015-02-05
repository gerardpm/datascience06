
# coding: utf-8

# In[2]:

import matplotlib.pyplot as plt


# In[3]:

x = [2,2,2,2,4,5,6,6,6,6,6,7,8,8,8,8,9,9,9,4,4,4,4,0,0,0,5,5,5,]


# In[4]:

plt.boxplot(x)
plt.show()


# In[5]:

plt.hist(x, histtype ='bar')
plt.show()


# In[6]:

import numpy as np


# In[7]:

import scipy.stats as stats


# In[8]:

import matplotlib.pyplot as plt


# In[9]:

plt.figure()


# In[10]:

test_data = np.random.normal(size = 1000)


# In[11]:

graph1 = stats.probplot(test_data, dist = "norm", plot = plt)


# In[12]:

plt.show()


# In[13]:

test_data2 = np.random.uniform(size = 1000)


# In[14]:

graph2 = stats.probplot(test_data2, dist = "norm", plot = plt)


# In[ ]:

plt.show()


# In[ ]:



