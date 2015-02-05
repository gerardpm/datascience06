
# coding: utf-8

# In[34]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_country-90m.csv', 'rU') as inputFile:
    pass


# In[27]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_country-90m.csv', 'rU') as inputFile:
    for line in inputFile:
        print line


# In[38]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_country-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
            print line


# In[40]:

with open ('C:\Users\gerar_000\Projects\lecz-urban-rural-population-land-area-estimates-v2-csv\lecz-urban-rural-population-land-area-estimates_country-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        print line


# In[29]:

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
            print line


# In[30]:

header = header.rstrip().split(',')
print header


# In[31]:

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
            print line[0], line[5]


# In[32]:

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
            print line[0], line[5], type(line[5])


# In[33]:

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            print line[0], line[5], type(line[5])


# In[34]:

import collections


# In[42]:

population_dict = collections.defaultdict(int)

    


# In[45]:

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]


# In[46]:

with open('national_population.csv','w') as outputFile:
    outputFile.write('continent,2010_population\n')


# In[47]:

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')


# In[48]:

import collections
population_dict = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population\n')

    for k, v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')


# In[ ]:



