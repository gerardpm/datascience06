
# coding: utf-8

# In[2]:

import sqlite3 as lite


# In[3]:

con = lite.connect('getting_started.db')


# In[5]:

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data


# In[ ]:

imp

