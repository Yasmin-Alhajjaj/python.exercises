#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:25:23 2019

@author: owner
"""
#Q1
'''
num1,num2=input("insert two number ??\t").split()
max=num1 if (int(num1)>int(num2)) else num2
print("the greatest:\s",max)
'''

#Q2
''''
num=int(input("Input a number:\t"))
for a in range (1,11):
    print(num,"*",a,"=",num*a)
 '''
 
#Q3
'''
star=["*","**","***","****","*****"]
stars=["****","***","**","*"]

for i in star:
    print(i)
for i in stars:
    print(i)
'''

"""
for a in range (10):
   if a<6:
       for i in range(a):
            print("*",end="")
   else:
       for r in range(10-a):
            print("*",end="")
   print()    
"""

#Q4
"""
letters=["x","y","z","a","b","c"]
for i in letters:
    if i=="a":
        continue
    elif i=="c":
        break
    print(i)
'''    
#out x
y
z
b
'''
"""

#Q5
"""
for x in range(12,25,3):
    print(x)
'''   
#out
12
15
18
21
24
'''
"""

#Q6
"""
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
'''    
    #out
1
2
3    
'''
"""    
    
#Q7
'''
sum=0
num=int(input("plaece insert num??\t"))
for i in range(num+1):
    sum=sum+i
print(sum)
 '''
 #Q8
"""
num=int(input("plaece insert num??\t"))
if (num%2)==0:
    print("number",num,"is even")
else:
    print("number",num,"is odd")
 """ 
    
#Q9
 #1
'''
for s in range(3):
    for d in range(2-s):
        print(" ",end="")
    for d in range(s+1):
        print("*",end="")
    for d in range(s):
        print("*",end="")      
    print()
for s in range(2):
    for d in range(s+1):
        print(" ",end="")
    for d in range(2-s):
        print("*",end="")
    for d in range(2-(s+1)):
        print("*",end="")      
    print()
'''
#2
'''
for s in range(15):
    for d in range(14-s):
        print(" ",end="")
    for d in range(s+1):
        print("*",end="")
    for d in range(s):
        print("*",end="")      
    print()
for s in range(14):
    for d in range(s+1):
        print(" ",end="")
    for d in range(14-s):
        print("*",end="")
    for d in range(14-(s+1)):
        print("*",end="")      
    print()
'''
#3
'''
for s in range(3):
    y=0
    for d in range(2-s):
        print(" ",end="")
    for d in range(s+1):
        y=y+1
        print(y,end="")
    for d in range(s):
        y=y-1
        print(y,end="")      
    print()
for s in range(2):
    y=0
    for d in range(s+1):
        print(" ",end="")
    for d in range(2-s):
        y=y+1
        print(y,end="")
    for d in range(2-(s+1)):
        y=y-1
        print(y,end="")      
    print()
 '''
 #4
''' 
for s in range(9):
    y=0
    for d in range(8-s):
        print(" ",end="")
    for d in range(s+1):
        y=y+1
        if y>9:break
        print(y,end="")
    for d in range(s):
        y=y-1
        if y<1:break
        print(y,end="")      
    print()
for s in range(8):
    y=0
    for d in range(s+1):
        print(" ",end="")
    for d in range(8-s):
        y=y+1
        if y>9:break
        print(y,end="")
    for d in range(8-(s+1)):
        y=y-1
        if y<1:break
        print(y,end="")      
    print()
'''
 
 #5 the best sol
for s in range(9):
    y=1
    for d in range(8-s):
        print(" ",end=" ")
    for d in range(s+1):
        print(y,end=" ")
        y=y+1
    y=y-2
    for d in range(s):
        print(y,end=" ")
        y=y-1
    print()
for s in range(8):
    y=1
    for d in range(s+1):
        print(" ",end=" ")
    for d in range(8-s):
        print(y,end=" ")
        y=y+1
    y=y-2
    for d in range(8-(s+1)):
        print(y,end=" ") 
        y=y-1
    print()
 
#Q10
"""
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No integer! Please try again ...")
print(n)
"""
      
#Q11
"""
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b=",b)
except(ZeroDivisionError,NameError):
    print("\nError")
    #out
    '''
    Error
'''
"""




    
    