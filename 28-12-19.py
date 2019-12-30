#!/usr/bin/env python
# coding: utf-8

# # collection types in python
# # List 
# # Tuple
# # Set
# # Dictionary
# # List:it is ordered and mutable and allows duplicate numbers
# # Tuple:it is ordered and immutable, allows duplicate numbers
# # set:it is unordered and unindexed, no duplicate members 
# # dictionary:it is unordered,mutable and indexed,no duplicates

# # list represents group of elements
# # list can store different types of elements
# # size of list can be changable
# #list can be represented as [],all items are separated by a comma
# #syn:
# list_name=[e1,e2,e3.....en]
# li=[12,56.7,'gitam','hyd','dhyanhitha']
# li=[] #empty list

# In[2]:


a=[12,56,89,100.6,'gitam']
print(a)
print(type(a))


# In[3]:


b=[34,70,19,100,56,34]
for ele in b:
    print(ele,end=" ")
print()
for i in range(len(b)):
    print(b[i],end=" ")
print()
i=0
while(i<len(b)):
    print(b[i],end=" ")
    i=i+1


# In[5]:


help("list")


# In[6]:


b


# In[7]:


print(b[5])


# In[8]:


print(b[2])


# In[9]:


b[5]


# In[10]:


b[4]=8989


# In[11]:


print(b[4])


# In[12]:


b


# In[13]:


#del is used to delete an item from a list or complete list also
a


# In[14]:


del a[0]


# In[18]:


a


# In[19]:


del a


# In[23]:


#append():
# it is used to add an item at the end of lisst
#syn:
# list_name.append(element)
print(b)
b.append(500)
b


# In[27]:


# insert()
# we can add a element at specific index
# syn:
# list_name.insert(index,element)
print(b)
b.insert(2,0)
b


# In[28]:


print(b)
b.append(9)
b


# In[29]:


# pop()
# it is used to remove the list element from list
# pop(n)
# it is used to remove the element at specific index
# syn:
# list_name.pop(index)
# remove(n):
# it is used to remove the element
# list_name.remove(index)


# In[30]:


b.pop()


# In[32]:


b.pop(2)


# In[37]:


b.remove(500)
b


# In[40]:


c=[100,20,25,100,5,213,100,25]
print(c)


# In[41]:


b.remove(100)


# In[43]:


c.remove(25)
c


# In[44]:


b.reverse()


# In[45]:


b


# In[46]:


c.index(100)


# In[53]:


b.sort()
print(b)
b.reverse()
b


# In[54]:


max(b)


# In[57]:


min(b)


# In[58]:


sum(c)


# In[59]:


b.clear()
b


# In[63]:


a=[]
n=int(input('enter the size'))
for i in range(n):
    a.append(int(input("enter the element")))
for ele in a:
    print(ele,end=" ")


# In[64]:


print(a[-1])


# In[66]:


print(a[1:5:2])


# In[68]:


print(a[::-1])


# In[ ]:




