#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[23]:


# Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[25]:


# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(" Even")
else:
   print("Odd")


# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


# Python program to find the largest number among the three input numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# In[21]:


# This program adds two numbers

num1 =int(input("enter num1:"))
num2 =int(input("enter num2:"))

sum = num1 + num2
print(sum)


# In[ ]:





# In[22]:


#addition 
num1=int(input("enter 1st num1:"))
num2=int(input("enter 2nd num2:"))

num3=num1+num2
print(num3)


# In[24]:


#subtrction
n1=int(input("enter 1st no."))
n2=int(input("enter 2nd no."))
n3=n1-n2
print(n3)


# In[27]:


#odd or even
num=int(input("enter number:"))
if num%2==0:
    print("even")
else:
    print("odd")
    


# In[28]:


#swaping 2 numbers
n1=int(input("enter number n1:"))
n2=int(input("enter number n2:"))

temp=0
temp=n1
n1=n2
n2=temp

print("n1 after swapping",n1)
print("n2 after swapping",n2)


# In[29]:


#prime number 
first=int(input("enter starting number:"))
last=int(input("enter ending number:"))

for num in range(first, last+1):
    if num>1:
        for i in range(2, num):
            if (num%i)==0:
                break
        else:
            print(num)


# In[36]:


#check prime number
num=int(input("enter number:"))

flag=False

if num > 1:
    for i in range(2,num):
        if num % i== 0:
            flag=True
            break
if flag:
    print("number is not prime")
else:
    print("number is prime")


# In[17]:


#first even number
#first=int(input("enter first number "))
last= int(input("enter last number"))

for num in range(0, last, 2):
    print(num)


# In[18]:


#first odd numbers
#first=int(input("enter first number "))
last= int(input("enter last number"))

for num in range(1, last, 2):
    print(num)


# In[4]:


#amstrong number
num=int(input("enter number:"))
temp=num
sum=0

while temp > 0:
    digit = temp%10
    sum += digit**3
    temp //= 10
    
if num==sum:
    print("amstrong")
else:
    print("not amstrong")


# In[10]:


#pallimdron
my_str= "mnoPOnM"
#my_str='aIbohPhoBiA'
my_str=my_str.casefold()

rev_str= reversed(my_str)

if list(rev_str) == list(my_str):
    print("Palliomdrom")
else:
    print("not Palliomdrone")


# In[12]:


#factorization
num=int(input("enter number:"))
fact=1

if num<0:
    print("sorry, factorial not for negative numbers")
elif num ==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
        


# In[ ]:




