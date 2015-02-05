
# coding: utf-8

# In[1]:

if 5 > 3:
    print("Yep, math works today.")


# In[2]:

if 5 < 3:
    print("Things might be a little off...")
else:
    print("Yep, math works today.")


# In[3]:

if 5 < 3:
    print("Things might be a little off...")
elif 5 == 3:
    print("Maybe we should stay inside.")
else:
    print("Yep, math works today.")


# In[9]:

labels = {"Lookout Records": "2001-2006",
               "Touch and Go": "2007-2009",
               "Matador": "2010-present"}


# In[12]:

labels.keys()


# In[13]:

print labels


# In[14]:

labels.values()


# In[18]:

lookout_set = {2001,2002,2003,2004,2005,2006}


# In[19]:

lookout_set


# In[20]:

matador_set = {2010,2011,2012,2013,2014,2015}


# In[22]:

matador_set


# In[23]:

touchngo_set = {2007,2008,2009}


# In[29]:

touchngo_set


# In[38]:

if 2007 > 2006:
    print ("Lookout Records")
elif 2010 < 2009:
    print ("Matador Records")
else: 
    print ("TouchandGo")


# In[1]:

beatles = ("John", "Paul", "George", "Ringo")


# In[3]:

for beatle in beatles:
    print beatle


# In[4]:

for n in range(1,100):
    if n % 3 == 0:
        print(n)
else:
    print("The loop is over")


# In[11]:

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}


# In[12]:

for actor in actors: 
    print actor


# In[13]:

miles_run = 0
running   = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False
else:
    print("Whew! I'm tired")


# In[16]:

miles_run = 0
running   = True

while running:
    if miles_run <=120:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 2
    else:
        running = False
else:
    print("Whew! I'm tired")


# In[17]:

1 /0


# In[18]:

a = 1
b = 0
try:
    a / b
except ZeroDivisionError:
    print "Cannot divide by zero."


# In[40]:

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

try:
   phone_book = "Jamie Winston"
    
except SyntaxError:
    print "No number found."


# In[41]:

for i in range(1,10):
     print i


# In[42]:

import collections


# In[43]:

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
count_dict = collections.defaultdict(int)
for i in number_list:
    count_dict[i] += 1


# In[44]:

a = 2
a += 2
print a


# In[45]:

def addition(a, b):
    return a + b


# In[46]:

print addition(2,2)


# In[47]:

print addition("Hi ", "There")


# In[57]:

with open('C:\Users\gerar_000\Desktop\Data Science\Courses\Thinkful\lecz-urban-rural-population-land-area-estimates-v2-csv', 'rU') as inputFile:
 pass


# In[ ]:

interest = 0
paying   = True

while paying:
    if interest <= 400000:
        print("Still paying! On year {}".format(interest))
        Interest += 20000
    else:
        paying = False
else:
        print("Whew! I'm tired")


# In[ ]:



