
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

data = [i.split(', ') for i in data] 


# In[4]:

column_names = data[0]


# In[5]:

data_rows = data[1::]


# In[6]:

df = pd.DataFrame(data_rows, columns=column_names)


# In[7]:

from scipy import stats


                print 'Tobacco'
                
# In[ ]:



