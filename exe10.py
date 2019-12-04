#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:11:17 2019

@author: owner
"""

# k ) Plot in 3dimention f = x * * 2 * 7 * * 3 ( x , - , 6 ) , ( y , - 6 , 6 ) ) Agenda





#Q1
#1
import sympy as sym
x,y,i,n,z = sym.symbols('x y i n z')
expr = x**2+x**3+21*x**4+10*x+1
print ( expr.subs(x, 7) )

#2
print(sym.expand((x + y) ** 2 ))

#3
print( sym.simplify( (4*x**3+21*x**2+10*x+12 )))

#4
print(sym.limit( 1/(x**2),x,sym.oo ))

#5
print(sym.summation(2*i+i-1,(i,5,n)))

#6
print(sym.integrate(sym.sin(x)+sym.exp(x)*sym.cos(x)+sym.tan(x),x))

#7
print(sym.factor(x**3+12*x*y*z+3*y**2*z))


#8
print (sym.solveset( x-4,x) )

#9
m1 = sym.Matrix([ [ 5 , 12 , 40 ] ,[ 30 , 70 , 2 ]])
m2 = sym.Matrix([ 2 , 1 , 0 ])
print( m1*m2 )

#10
from sympy.plotting import plot
plot(x**3+3, (x, -10, 10))


#11
from sympy.plotting import plot3d
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))



#Q2
import xlsxwriter
workbook = xlsxwriter.Workbook('exe10.xlsx')
worksheet = workbook.add_worksheet()
worksheet.autofilter('A1:B1')
data = ['This is Example']
format1 = workbook.add_format({'bold' : True, 'font_color': 'red'})
worksheet.write_column('A1:B1', data, format1)

data2 = ['example',1,2]
format2 = workbook.add_format({ 'font_color': 'black'})
worksheet.write_column('A2:a4', data2, format2)

data3 = [3]
#format1 = workbook.add_format({'bold' : True, 'font_color': 'red'})
worksheet.write_column('A5', data3, format1)

workbook.close()


#Q3
from xlrd import open_workbook
wb = open_workbook('exe3.xlsx')
for s in wb.sheets():
    print ("Sheet:", s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
        values.append(s.cell(row,col).value)
    print(values)






