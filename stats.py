
# coding: utf-8

# In[11]:

import pandas as pd


# In[12]:

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


# In[13]:

data = data.splitlines()


# In[14]:

data = [i.split(', ') for i in data]


# In[15]:

column_names = data[0]


# In[16]:

data_rows = data[1::]


# In[17]:

df = pd.DataFrame(data_rows, columns=column_names)


# In[18]:

from scipy import stats


# In[19]:

df['Alcohol'] = df['Alcohol'].astype(float)


# In[20]:

df['Tobacco'] = df['Tobacco'].astype(float)


# In[21]:

df['Alcohol'].mean()


# In[52]:

df['Alcohol'].mean()


# In[22]:

df['Alcohol'].median()


# In[23]:

stats.mode(df['Alcohol'])


# In[24]:

df['Tobacco'].mean() 


# In[15]:

df['Tobacco'].median()


# In[25]:

stats.mode(df['Tobacco'])


# In[26]:

max(df['Alcohol']) - min(df['Alcohol'])


# In[27]:

df['Alcohol'].std()


# In[28]:

df['Alcohol'].var()


# In[20]:

max(df['Tobacco']) - min(df['Tobacco'])


# In[21]:

df['Tobacco'].std()


# In[30]:

df['Tobacco'].var()


# In[40]:

df ['Tobacco'].var()


# In[53]:

print df['Tobacco'].var()


# In[86]:

var1 = 'The mean of '
var2 = 'The mode of '
var3 = 'The variance of '
var4 = 'The standard deviation of '
var5 = 'The range of '
var6 = 'The median of ' 
var7 = 'Alcohol and Tobacco are'


# In[82]:

print var1 + var9
print df['Alcohol'].mean() 
print df['Tobacco'].mean()


# In[87]:

print var6 + var7
print df['Alcohol'].median()
print df['Tobacco'].median()


# In[88]:

print var4 + var7
print df['Alcohol'].std()
print df['Tobacco'].std()


# In[89]:

print var3 + var7
print df['Alcohol'].var()
print df['Tobacco'].var()


# In[90]:

print var5 + var7
print max(df['Alcohol']) - min(df['Alcohol'])
print max(df['Tobacco']) - min(df['Tobacco'])


# In[ ]:



