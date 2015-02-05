
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

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


# In[3]:

data = data.splitlines()


# In[4]:

data = [i.split(', ') for i in data]


# In[5]:

column_names = data[0]


# In[6]:

data_rows = data[1::]


# In[7]:

df = pd.DataFrame(data_rows, columns=column_names)


# In[8]:

from scipy import stats


# In[9]:

df['Alcohol'] = df['Alcohol'].astype(float)


# In[10]:

df['Tobacco'] = df['Tobacco'].astype(float)


# In[11]:

df['Alcohol'].mean()


# In[12]:

df['Alcohol'].median()


# In[13]:

stats.mode(df['Alcohol'])


# In[14]:

df['Tobacco'].mean() 


# In[15]:

df['Tobacco'].median()


# In[16]:

stats.mode(df['Tobacco'])


# In[17]:

max(df['Alcohol']) - min(df['Alcohol'])


# In[18]:

df['Alcohol'].std()


# In[19]:

df['Alcohol'].var()


# In[20]:

max(df['Tobacco']) - min(df['Tobacco'])


# In[21]:

df['Tobacco'].std()


# In[22]:

df['Tobacco'].var()


# In[ ]:

df

