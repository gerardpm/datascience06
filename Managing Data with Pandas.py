
# coding: utf-8

# In[3]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_codebook.csv', 'rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print line


# In[4]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_codebook.csv', 'rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print len(line)


# In[15]:

import csv

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_country-90m.csv', 'rU') as inputFile:
     inputReader = csv.reader(inputFile)
     for line in inputReader:
         print line


# In[17]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_codebook.csv', 'r') as inputFile:
     inputReader = csv.reader(inputFile)
     for line in inputReader:
        print len(line)


# In[18]:

import pandas as pd


# In[24]:

input_dataframe = pd.read_csv ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_continent-90m.csv') 


# In[25]:

input_dataframe['Continent']


# In[26]:

input_dataframe[0:10]


# In[ ]:



