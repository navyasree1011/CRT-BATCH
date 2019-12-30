#!/usr/bin/env python
# coding: utf-8

# # control structres:
# # for loop
# # while loop
# ## for loop:
# ## for var in sequence/object
#      statement-s
# # or
# ### for var in range(start,stop,step):
#      statements
# ### while condition:
#      statements
#      

# In[2]:


n=int(input("enter the range"))
for i in range(1,n+1):
    print(i,end=" ")
    


# In[5]:


for i in range(6):#6 is stop and start=0
    print(i,end=" ")
print()
for i in range(1,6):#start is 1 and stop is 6
    print(i,end=" ")
print()
for i in range(1,10,2):# start is 1,stop=10,step=2
    print(i,end=" ")


# In[7]:


n=int(input(" "))
sum=0
for i in range(i,n+1):
    sum=sum+i
print(sum)


# In[11]:


str1="gitamhyd"
for i in range(len(str1)):
    print(str1[i],end=" ")
print()
for i in str1:
     print(i,end=" ")          


# In[13]:


a=[12,89,90,45,6]
for i in a:
    print(i,end=" ")
print()
for i in range(len(a)):
    print(a[i],end=" ")


# print 1 to n numbers using while

# In[15]:


n=int(input(" "))
i=1
while(i<=n):
    print(i,end=" ")
    i=i+1


# In[16]:


# input:123
#output: 3 2 1 


# In[21]:


n=int(input(" "))
while(n!=0):
    r=n%10
    print(r,end=" ")
    n=n//10


# In[25]:



#input:1947
#output:21
n=int(input(" "))
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)


# # reverse of a number

# In[29]:


#input:1947
#output:7491
n=int(input(" "))
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)


# # to find a number is palindrome or not

# In[32]:


#input:121
#output:121
n=int(input(" "))
num=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(rev==num):
    print("palindrome")
else:
    print("not a palindrome")


# In[33]:


#input:1947
#output:9
n=int(input(" "))
max=0
while(n!=0):
    r=n%10
    if(r>max):
        max=r
    n=n//10
print(max)


# ### smallest digit of a number

# In[34]:


#input:2971
#output:1
n=int(input(" "))
min=9
while(n!=0):
    r=n%10
    if(r<min):
        min=r
    n=n//10  
print(min)


# ### factorial of a number

# In[35]:


#input:5
#output:120
n=int(input(" "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)


# ### factorial of a number while loop
# 

# In[37]:


n=int(input(" "))
i=1
f=1
while(i<=n):
    f=f*i
    i=i+1
print(f)    


# # user define function
# # def func_name(<parameters>)
#           statements
#           return

# In[38]:


def add(a,b):
    return a+b
print(add(12,78))# fn call


# In[39]:


def add(a,b):
    c=a+b
    return c
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(add(a,b))


# ###  find the sum of even digit of a given number

# In[2]:


def evenDigitSum(n):
    sum=0
    while(n!=0):
        r=n%10
        if(r%2==0):
            sum=sum+r
        n=n//10
    return sum
n=int(input(" "))
print(evenDigitSum(n))


# In[11]:


def factors(n):
    for i in range(1,n+1):
        if(n%i==0):
             print(i,end=" ")
    return 
n=int(input(" "))
factors(n)


# In[19]:


#input:16783
#output:[1,6,7,8,3]
def numList(n):
    a=[]
    while(n!=0):
        r=n%10
        a.append(r)
        n=n//10
    a.reverse()
    return a
print(numList(16783))


# ### to find given no. is prime or not

# In[29]:


num=407
if num>1:
    for i in range(2,num):
        if(num % i)==0:
            print(num,"is not a prime number")
            break
    else:
            print(num,"is a prime number")
else:
            print(num,"is not prime number")


# In[ ]:


if num>1:
    for i in range(1,n):
        if(num % i)==0:
            print(num)

