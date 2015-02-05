
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[2]:

import numpy as np


# In[3]:

import matplotlib.mlab as mlab


# In[4]:

mean = 0


# In[5]:

variance = 1


# In[6]:

sigma = np.sqrt(variance)


# In[8]:

x = np.linspace(-3,3,100)


# In[ ]:

plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()


# In[15]:

import collections


# In[16]:

testlist = [1,4,5,6,9,9,9]


# In[17]:

c = collections.Counter(testlist)


# In[18]:

print c


# In[19]:

count_sum = sum(c.values())


# In[20]:

print count_sum


# In[21]:

print sum(c.values())


# In[26]:

for k,v in c.iteritems():
    print "The frequency of number " + str(k) + " is " + str(float(v)/count_sum)


# In[27]:

import matplotlib.pyplot as plt


# In[28]:

x = [1,1,1,1,1,1,1,1,2,2,2,3,4,4,4,4,5,6,6,6,7,7,7,7,7,7,7,7,8,8,9,9]


# In[29]:

plt.boxplot(x)


# In[30]:

plt.show()


# In[32]:

plt.hist(x, histtype ='bar')


# In[33]:

plt.show()


# In[34]:

import numpy as np


# In[35]:

import scipy.stats as stats


# In[36]:

import matplotlib.pyplot as plt


# In[38]:

plt.figure()


# In[39]:

test_data = np.random.normal(size = 1000)


# In[40]:

graph1 = stats.probplot(test_data, dist ="norm", plot = plt)


# In[41]:

plt.show()


# In[44]:

plt.figure()


# In[45]:

test_data2 = np.random.uniform(size = 1000)


# In[46]:

graph2 = stats.probplot(test_data2, dist = "norm", plot = plt)


# In[47]:

plt.show()


# In[ ]:



