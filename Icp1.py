#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Write a python program for the following:
#Input the string “Python” as a list of characters from console, delete at least 2 characters, reversethe resultant string and print it.

x = input("Enter the string :")
y =list(x.strip())
print(type(y))
print(y)
y.pop(-3)
y.pop(-3)
print(y)
y.reverse()
x = ''.join(y)
print(x)


# In[2]:


#Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
# declaring a string variable
s = input("Enter the sentence :")

# replacing string python with pythons
s = s.replace('python', 'pythons')
print("Updated string is : ")
print(s)


# In[3]:


#Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.

score = int(input("Enter the score of the person: "))
if score >= 90:
    print("A grade")
elif score >=80:
    print("B grade")
elif score >=70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("Fail grade")


# In[ ]:




