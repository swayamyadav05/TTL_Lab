#!/usr/bin/env python
# coding: utf-8

# In[5]:


print ("Hello World")


# In[6]:


x=5
y=7
print (x+y)


# In[7]:


print (10+39)


# In[8]:


name=input()
print("My name is "+ name)


# In[10]:


name=input("Enter your name:")
print("My name is "+name)


# In[17]:


x=str(7)
y=str(4)

if x>y:
    print(x+" is greater")
elif x==y:
    print(x+" = "+y+ "are equal")
else:
    print(y+" is greater")


# In[26]:


x=(input("Enter x: "))
y=(input("Enter y: "))

if x>y:
    print("Greater number is: "+x)
elif x==y:
    print(x+" and "+y+" are equal")
else:
    print("Greater number is: "+y)


# In[27]:


r=5
l=8
b=4
h=12
AoC=str(3.14*r*r)
AoS=str(l*l)
AoR=str(l*b)
AoT=str(0.5*b*h)
print("Area of Circle is "+AoC)
print("Area of Square is "+AoS)
print("Area of Rectangle is "+AoR)
print("Area of Triangle is "+AoT)


# In[31]:


marks=int(input("Enter you marks: "))
match marks:
    case O if O>89:
        print("O Grade")
    case E if E>79:
        print("E Grade")
    case A if A>69:
        print("A Grade")
    case B if B>59:
        print("B Grade")
    case C if C>49:
        print("C Grade")
    case D if D>39:
        print("D Grade")
    case _:
        print("FAIL")


# In[ ]:





# In[ ]:




