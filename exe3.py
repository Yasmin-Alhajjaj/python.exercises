#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:13:40 2019

@author: owner


7. Write a Python program to iteration over sets, use the set num_set = set([0, 1, 2, 3, 4, 5])
"""
"""
#Q1
list=[1,2,3,4,5]
for a in list:
    print(a)

#Q2
list=[1,2,3,4,5]
print(sum(list))


#Q3
list=[1,2,3,4,5]
print(max(list))

#Q4
list = [10,20,30,20,10,50,60,40,80,50,40]
print(set(list))

#Q5
list=[1,2,3,4,5]
if len(list)==0:
    print("the list is empty")
else:
    print("the list is not empty")


#Q6
list = (10,"20",[30,20,10,50])
for a in list:
    print(a)
    
#Q7
num_set = set([0, 1, 2, 3, 4, 5])
for a in num_set:
    print(a)

#Q8
set1={1,2,3,"r"}
set2={1,3,"R","r"}
print(set1 & set2)


#Q9
setx= set(["green","blue"])
sety= set(["blue","yellow"])
seta=setx | sety
print(seta)

#OUT
"""
{'blue', 'green', 'yellow'}
"""

#Q10
seta=set([5,10,3,15,2,20])
print(len(seta))

#OUT
'''
6
'''
#Q11
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
 #OUT
'''
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
  

#Q12
a="Hello World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))

#OUT
'''
e
llo
orl
12
hello world!
Jello World!
'''
"""



