#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:01:00 2019

@author: owner
"""

'''
#Q1
o= lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))


#Q2
num = [1,2,3,4,1]
x= reduce(lambda a,b: a*b,num)
print(x)

#Q3

num1 = [1,2,3,4,1]
num2 = [1,2,3,4,1]
print(list(map(lambda a,b:a*b,num1 ,num2)))


#Q4
x =list(filter(lambda y:y<0,range(-5,5)))
print(x)



#Q5
x= lambda a,b,c : a+b+c
print(x(5,6,2))
#out
"""
13
"""

#Q6

x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Countney")

result = list(zip(x,y,z))
print(result)

#out
[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]


#Q7

coin=('Bitcoin','Ether','Ripple','litecoin')
code=('BTC','ETH','XRP','LTC')
d= dict(zip(coin,code))
print(d)

#out
{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'litecoin': 'LTC'}


#Q8
def fun(var):
    letters=['a','e','i','o','u']
    if(var in letters):
        return True
    else:
        return False
    
seq=['g','j','e','j','k','o','p','r']
f=list(filter(fun,seq))
print(f)
#OUT
['e', 'o']



#Q9
x= list(map(int,input("Enter a mult:").split()))
print(x)
#OUT
[4, 8, 2]


#Q10

[1,4,9,4,16]



#Q11
def fun(a,b):
    return a+b
a=list(map(fun,[2,4,5],[1,2,3,2,4]))
print(a)

#OUT
[3, 6, 8]



#Q12
c=map(lambda x: x+x, filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))

#out
[6, 8]




#Q13
[4,6,8]

#Q14

x= reduce(lambda x,b: x if x<b else b , [8,2,5,6,4,25] )
print(x)
'''
#Q15

n=[1,2,3]
l=['a','b','c']
x=tuple(zip(n,l))
print(x)


