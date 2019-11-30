#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:29:34 2019

@author: owner
"""

#Q1
import pandas as pd

data = [2, 4, 6, 8, 10]
s = pd.Series(data)
#print(s)

#Q2

s = pd.Series([100, 200,300,400,800],index=['a', 'b', 'c', 'd', 'e'])
#print(s)

#Q3

data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)
#print( s.describe())
#s.plot(kind="bar")


#Q4

Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200]}
df = pd.DataFrame(Data,columns=["d1", "d2"])
#df.plot()

#Q5
import pandas as pd

data= {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
#print(pd.DataFrame(data))


#Q6
series = pd.Series([968, 155, 77, 578, 973],index=['Bob','Jessica','Mary','John','Mel'])
#print(series)
#series.plot.pie(y='births', figsize=(5, 5))


#Q7 
df= pd.DataFrame([1,2,3,4,5,6,7,8,9], columns = ['Number'])
df.to_csv('myDataFrame.csv', sep='\t')
df= pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)
print(df)



#Q8
"""
import numpy as np

date = pd.date_range('20000101', periods = 4)

df = pd.DataFrame(np.random.randn(4, 2), index = date, columns = ['A', 'B'] )

print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104', ['A']])
print(df.iloc[:, 1:2])
print(df[df.B > 0])
df['A'] = [100, 200, 300, 100]
print(df)
print(df[df['A'].isin([200, 300])])
"""

