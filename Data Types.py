
# coding: utf-8

# In[14]:

print "Hello World"


# In[15]:

t = True


# In[16]:

type(t)


# In[17]:

bool(42)


# In[18]:

bool("Happy go lucky")


# In[19]:

bool(0)


# In[20]:

bool("")


# In[22]:

a = 10


# In[23]:

b = 12


# In[25]:

answer = a >= b


# In[26]:

answer


# In[27]:

(a == a) and (b != a)


# In[28]:

(a == b) or (b == b)


# In[29]:

not(True)


# In[30]:

not(a != a)


# In[31]:

"This is a string."


# In[12]:

"This is " + "a string."


# In[13]:

"{0} don't think it {1} like it is, but it {2}".format("They", "be", "do")


# In[32]:

"Yar matey!"[0]


# In[33]:

li = []              # An empty list!


# In[34]:

other_li = [1, 2, 3] # A prefilled list!


# In[35]:

li.append(1)


# In[36]:

li.append(5)


# In[37]:

li.append(3)


# In[38]:

li


# In[40]:

li.pop()


# In[41]:

li


# In[42]:

li[0]


# In[43]:

li = [1, 2, 4, 3, 5]
# Select a range between index 1 and 3 (closed/open range, in math terms)


# In[51]:

li[1:3]
# Omit the beginning or end


# In[46]:

li[2:]


# In[47]:

li[:3]


# In[50]:

# Select every second entry (i.e. step by 2)
li[::2]


# In[52]:

# Reverse the list
li[::-1]
# Note the syntax for the above is: li[start:end:step]


# In[53]:

# Delete the 3rd item
del li[2]


# In[54]:

li


# In[56]:

# Check if 1 is in list li
1 in li


# In[57]:

# What's the length of the list li?
len(li)


# In[58]:

tup = (1, 2, 3)


# In[59]:

tup.append(4)


# In[60]:

tup + (4, 5, 6)


# In[61]:

tup


# In[63]:

new_tup = tup + (4, 5, 6)


# In[65]:

new_tup


# In[66]:

bookmark = (42, 5) # page number, line number


# In[68]:

bookmark1 = (35, 5)
bookmark2 = (86, 15)
bookmark3 = (106, 11)
notes = [bookmark1, bookmark2, bookmark3]


# In[69]:

print notes


# In[70]:

my_set = {1, 2, 2, 3, 4, 5, 6, 7}


# In[71]:

my_set


# In[72]:

your_set = {6, 7, 8, 9, 10}


# In[73]:

your_set


# In[74]:

my_set & your_set 


# In[75]:

my_set | your_set


# In[76]:

my_set - your_set


# In[77]:

1 in my_set


# In[78]:

stooges = {"Larry": "balding, with frazzled hair",
               "Curly": "short buzz-cut",
               "Moe"  : "bowl cut"}


# In[79]:

stooges


# In[80]:

stooges['Larry']


# In[81]:

stooges.keys()


# In[82]:

stooges.values()


# In[83]:

"Larry" in stooges


# In[84]:

stooges["Shemp"]


# In[86]:

stooges.get("Shemp")


# In[87]:

print(stooges.get("Shemp"))

