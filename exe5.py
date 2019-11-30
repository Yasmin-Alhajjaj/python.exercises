#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:20:09 2019

@author: owner
"""

#Q1
class Employee:
    
    def __init__(self,num, name,add,salary,job):
        self.Employee_Num = num
        self.__Name = name
        self.__Address = add
        self.__Salary = salary
        self.__Job = job

        
        
    def getName( self ):
        return "Name : " + self.__Name
    
    def getAddress( self ):
        return "Address : " + self.__Address
    
    def setAddress( self,newadd ):
        self.__Address=newadd
        
    def getnewAddress( self ):
        return "Address : " + self.__Address    
    
    def getSalary( self ):
        return ("salary :" , self.__Salary)
    
    def getJop( self ):
        return ("Job :" ,self.__Job)
    
    def __del__( self ):
        print ( self.__Name,"+ has deleted ")
        
    def getEmployee1( self ):
        print ("Name : " + self.__Name,"\n"
               "Address : " + self.__Address,'\n'
               "Job :" ,self.__Job,'\n'
               )
        
     
Employee1 = Employee(1,'mohad','amman,jordan',500,'Consultant')
'''
print(Employee1.getName())
print(Employee1.getAddress())
print(Employee1.getSalary())
Employee1.setAddress('Usa')
print(Employee1.getJop())
print(Employee1.getnewAddress())
'''
Employee1.getEmployee1()

del Employee1

print("\n/////////////////////////////\n")

Employee2 = Employee(2,'Hala Rana','Aqapa,jordan',750,'Manager')
print(Employee2.getName(),end="")
print(Employee2.getAddress(),end="")
print(Employee2.getSalary(),end="")
Employee2.setAddress('zarqaa')
#print(Employee2.getAddress(),end="")
print(Employee2.getJop())
del Employee2
