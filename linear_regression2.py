
# coding: utf-8

# In[3]:

import pandas as pd


# In[4]:

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[5]:

x = loansData['Interest.Rate'][0:5].values[1]


# In[6]:

y = lambda x: round(float(x.rstrip('%')) / 100,4)


# In[7]:

y


# In[8]:

y(x)


# In[9]:

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) /100,4))


# In[10]:

type(cleanInterestRate)


# In[9]:

cleanInterestRate[0:5]


# In[13]:

loansData['Loan.Length'][0:5]


# In[14]:

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))


# In[15]:

cleanLoanLength[0:5]


# In[16]:

loansData['Loan.Length'] = cleanLoanLength


# In[17]:

loansData['Loan.Length'][0:5]


# In[18]:

loansData['FICO.Range'][0:5]


# In[19]:

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-')[0])


# In[20]:

cleanFICORange[0:5]


# In[21]:

loansData.columns.values


# In[22]:

loansData['FICO.Score'] = cleanFICORange


# In[23]:

loansData['FICO.Range']


# In[24]:

loansData['FICO.Score']


# In[25]:

loansData['FICO.Score'].apply(float)


# In[26]:

loansData['FICO.Score']


# In[27]:

loansData['FICO.Score'] = loansData['FICO.Score'].apply(float)


# In[30]:

type (x)


# In[31]:

x


# In[32]:

loansData['Interest.Rate']


# In[33]:

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) /100,4))


# In[34]:

cleanInterestRate


# In[35]:

import numpy as np


# In[36]:

import pandas as pd


# In[37]:

import statsmodels.api as sm


# In[38]:

intrate = cleanInterestRate


# In[39]:

intrate


# In[40]:

loanamt = loansData['Amount.Requested']


# In[41]:

fico = loansData['FICO.Score']


# In[42]:

y = np.matrix(intrate).transpose()


# In[43]:

x1 = np.matrix(fico).transpose()


# In[44]:

x2 = np.matrix(loanamt).transpose()


# In[45]:

x = np.column_stack([x1,x2])


# In[46]:

x = sm.add_constant(x)


# In[47]:

model = sm.OLS(y,x)


# In[48]:

f = model.fit()


# In[49]:

print 'Coefficient: ',f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared


# In[51]:

# P-values of model = P-Values are extremely small hence no statistical
#signifcance; R2 = .66 and is below benchmark of .80 


# In[52]:

exit()


# In[ ]:



