#!/usr/bin/env python
# coding: utf-8

# # every variable in python is acts like object and object has 3 characteristics
# # identity
# # type
# #value

# In[1]:


a=10
print(id(a))
print(type(a))
print(a)


# In[2]:


b=10
b


# In[3]:


print(id(b))


# In[5]:


a=10
b=24.5
c="gitam"
d=2+4j
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))


# # number types
# ## integer
# ## float
# ## complex
# ## blooean
# ## all numbers are immutable,values are not 
# ## modified,if they modified new reference is
# ## pointing to modified value

# In[6]:


a=10
print(id(a))
a=100
print(id(a))


# In[7]:


a='t'
print(id(a))


# In[10]:


a=2+5j
print(a)
print(a.real)
print(a.imag)
print(a.conjugate())
c=complex(3,4)
print(c)


# In[12]:


c=2+5j
d=5+7j
print(c+d)
print(c-d)
print(c*d)


# In[14]:


str="gitam"
str1='gitam'
print(str)
print(str1)
print(type(str),type(str1))
print(len(str))


# # type convertions
# ## int()
# ## float()
# ## complex()
# ## list()
# ## tuple()
# ## set()
# ## dict()
# ## bool()

# # input()
# ## it is used to give the input to the program
# ## and its return type is string and by
# ## using type convertions to convert it into
# ## other types

# In[15]:


a=input("enter the number")
print(type(a))
b=int(a)
print(type(b))


# In[16]:


# comments in the python

'''
document srting
'''


# In[17]:



'''
print("its given the description about resource of python")

'''


# In[19]:


b="1947"
print(type(b))
print(len(b))
c=int(b)
print(type(c))
#print(len(c))


# In[22]:


a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=a+b
print("the sum id",c)


# # types of operators:
# ## 1)arthmetic operators
#   ### +,-,*,/(decimal quetient),//(integer quetient),**,%
#   ### //(floor division)
#   ### %(remainder)
#   ### **(acts like pow),where arguments are integers 

# a=12
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)# division with decimal
# print(a//b)# floor dividion 
# print(a%b)#remainder
# print(a**b)#pow(a,b)

# ## relational operators:
# ### <,<=,>,>=,==,!=

# In[25]:


x=10
y=34
print(x<34)
print(x==y)
print(x!=y)
print(int(x>y))
print(int(y>x))


# # logical operators:
# ## and or not

# In[26]:


x=20
print(x>20 and x<30)
print(x>=30 or x<=20)
print(not(x))


# # membership operators:
# ## in,not in

# In[28]:


str1="gitam"
print('i' in str1)
print('z' not in str1)


# # identity operators:
# ## is,isnot

# In[29]:


a=45
b=89
print(a is b)
print(a is not b)


#  # bitwise ops:(work with 0 and 1)
#  ## &,|,<<,>>,~
#  ## <<leftshift
#  ## >>rightshift
#  ## ~(1's complement)

# # special ops:
# ## + and , are used for concatenation
# ## * repetation operator
# ## [start:stop:step] slice operator
# ## range(start,stop,step)
# ## indentation:
# ## it represents block or{} in c

# In[30]:


a=100
print("the value of a is",a)
c=[1,2,3]
d=[4,5,6]
print(c+d)
d="gitam"
print(d*3)
print(d[1:3])
print(list(range(1,10,2)))


# # control sattements
# ## 1) simple if statement
# ### if(condition):
#      statement1
#      statement2
# 

# In[31]:


a=int(input("enter the number"))
if(a>0): 
  print("it is +ve no")
if(a<0):
    print("it is -ve no")
    if(a==0):
        print("it is zero")


# ## control statements:
# ## 1) if-else statement
#   ### if (condition):
#       statement1
#       statement2
#  ### else:
#       statement1
#       statement2

# In[32]:


n=int(input("enter the number"))
if(n%2==0):
    print(n,"is even number")
else:
    print(n,"is odd number")


# In[39]:


yr=int(input("enter the year"))
if((yr%100!=0 and yr%4==0) or yr%400==0):
    print(yr,"is leap year")
else:
    print(yr,"is not leap year")


# ## control satements:
# ## 3) elseif statement
# ### if(condition):
#       satement1
#       statement2
# ### elseif(condition):
#       statement3
#       statement4
# ### else: 
#       statement5
#       statement6

# In[41]:


a=10
b=200
c=100
if(a>b and a>c):
    print(a,"is big")
elif(b>c):
    print(b,"is big")
else:
    print(c,"big")


# In[42]:


a=10
b=20
print("before swapoing",a,b)
a,b=b,a
print("after swapping",a,b)


# In[46]:


a=100
b=25

ch=int(input("enter the choice"))
if(ch==1):
    print("the addition is",a+b)
elif(ch==2):
    print("the subtraction is",a+b)
elif(ch==3):
    print("the multiplation is",a*b)
elif(ch==4):  
    print("the division is",a/b)
else:
    print("choose the choice from[1-4] only")


# In[48]:


ch=input("enter the charactor")
if(ch=='a' or ch=='e' or ch=='i'or ch=='o' or ch=='u'):
  print("it is vowel")
elif(ch=='A' or ch=='E' or ch=="I" or ch=='O' or ch=='U'):
  print("it is vowel")
else:
    print("it is consonant")


# In[ ]:




