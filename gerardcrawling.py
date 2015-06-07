
# coding: utf-8

# In[271]:

from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import pandas as pd
import time
import urllib2


# In[293]:

pages = {}
url = "http://www.capterra.com/project-management-software/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
r = requests.get(url)
pages[url] = r.text
    
time.sleep(1)


# In[295]:

all_features


# In[294]:

products = soup.findAll('div', {'class': 'card  zindex-hack  listing'})
print len(products)


# In[296]:

urls = soup.findAll('a',{'class':'spotlight-link'})
for url in urls:
    print "wwww.capterra.com" + url['href']+(',')
    
    #got the output I wanted


# In[298]:

cols = []


# In[301]:

rows = []
for url in urls:
    page = pages[url]
    soup = BeautifulSoup(page)
    name = soup.find('h1', {'itemprop': 'name'}).text
    print name
    # This should only run the first time
    has_feature = []
    missing_feature = []
    checklist = soup.findAll('ul', {'class': 'check-list'})
    close_to_price = checklist[1].findAll('div', {'class': 'cell seven-twelfths'})
    rawprice= close_to_price[0].text.replace('See pricing details', '').strip()
    # TODO: do some further extraction on this data
    lis = soup.findAll('li', {'class': 'ss-check'})
    for li in lis:
        has_feature.append(li.text)
    lis = soup.findAll('li', {'class': 'ss-delete color-gray'})
    for li in lis:
        missing_feature.append(li.text)
    has_feature_dict = defaultdict(int)
    for feature in has_feature:
        has_feature_dict[feature] = 1
    row = []
    row.append(name)
    if len(cols) == 0:
        all_features = has_feature
        all_features.extend(missing_feature)
        cols = ['product_name']
        cols.extend(all_features)
    for c in range(1, len(cols)):
        has = has_feature_dict[cols[c]]
        row.append(has)
    rows.append(row)
    
    ## Getting all of these key Errors


# In[262]:

print all_features


# In[300]:

df = pd.DataFrame(rows)
df.columns = cols
df


# In[ ]:



