#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:42:20 2019

@author: owner

"""
from functools import reduce

class person():
    def __init__(self,name,add):
           self._Name=name
           self._Address=add
    def getName( self ):
        return "Name : " + self._Name
    def setName( self,newname ):
        self._Name = newname   
    def getAddress( self ):
        return "Name : " + self._Name
    def setAddress( self,newadd ):
        self._Address = newadd    
    def __del__(self):
        print("I have been deleted")
        
class Employee(person):
    def __init__(self,num,name,Add,salary,job,lista):
        self.Employee_Num =int(num)
        super().__init__(name,Add)
        self.__Salary =float(salary)
        self.__Job =str(job)
        self.__loans=lista    
    def getSalary( self ):
        return  self.__Salary
    def getloans(self):
        return self.__loans    
    def setSalary( self,newsalary ):
        self._Name = newsalary   
    def getJobTitle( self ):
        return "job-Title : " + self.__Job
    def setJobTitle( self,newjob):
        self._Address = newjob  
    def getTotalLoans( self ):
        if len(self.__loans)>0:
            return(reduce(lambda x, y: x + y, self.__loans))
        else:
            return 0
    def getMaxLon( self ):
        max=reduce(lambda a,b: a if a>b else b,self.__loans)
        return max
    def getMinLon( self ):
        #return "MinLon : " + self.__loans
        if len(self.__loans)>0:
            min=reduce(lambda a,b: a if a<b else b,self.__loans)
            return int(min)
    def setLoans(self,newloans):
        self.__loans=newloans   
    def printinfo(self):
        print("Employee Number :", self.Employee_Num)
        print("Name :", self._Name)
        print("Address :", self._Address)
        print("Job Title :", self.__Job)
        print("Salary :", self.__Salary)
        print("Total Loans :", self.getTotalLoans())   
    def __del__(self):
        print("I have been deleted")

class Student(person):
    def __init__(self,num,name,Add,sub,marks):
        self.Student_Num =int(num)
        super().__init__(name,Add)
        self.__Subject=str(sub) 
        self.__Markst : " + self.__Subject
    def setSubject( self,newsub ):
        return "newSubject : " + self.__Subject   
    def getMarks( self ):
        return "Marks : " , self =dict(marks)    
    def getSubject( self ):
        return "Subjec.__Marks
    def setMarks( self,newMarks ):
        self.__Marks = newMarks  
    def getAverage( self ):
       avg=0
       for x in self.__Marks.values():
           avg=avg+x 
       return(avg/len(self.__Marks))
    def getA(self):
        A = list(filter(lambda x : self.__Marks[x] >= 90, self.__Marks))
        return A
    def printInfo(self):
        print("Student Number :", self.Student_Num)
        print("Name :", self._Name)
        print("Address :", self._Address)
        print("Subject :", self.__Subject)
        print("Student's Average:", self.getAverage())
    def __del__(self):
        print("I have been deleted")


Employee1=Employee(1000,"Ahmad Yazaan","Amman Jordan",500,"HR Consultant",[434,200,1020])
Employee2= Employee(2000,"Hala rana","Aqaba jordan", 750,"Manager",[150,3000,250])
Employee3= Employee(3000,"Mariam ali","Mafraq jordan", 600,"HR s",[304,1000,250,300,500,235])
Employee4= Employee(4000,"Yasmin mohameed","Karak jordan", 865,"Director",[])

Student1=Student(20191000,"Khalid Ali","Irbid Jordan", "History",{"English":80,"Arabic":90,"Art":95,"Management":75})
Student2=Student(20182000,"Reem Hani","Zarqa Jordan", "Softwere Eng",{"English":80,"Arabic":90,"Management":75,"Calculus":85,"OS":73,"Priogramming":90})
Student3=Student(20161001,"Nawras Abdallah","Amman Jordan", "Arts",{"English":83,"Arabic":92,"Art":90,"Management":70})
Student4=Student(20172030,"Amal Raed","Tafelah Jordan", "Computer Eng",{"English":83,"Arabic":92,"Management":70,"Calculus":80,"OS":79,"Priogramming":91})

#Q1
Employeelist=[Employee1,Employee2,Employee3,Employee4]

#Q2
studendsList=[Student1,Student2,Student3,Student4]

#Q3
def numberofEmpl (EmployeeList):
    print("----------Q3----------")
    print("Num of Employees :",len(Employeelist))
numberofEmpl(Employeelist)
    
#Q4
print("----------Q4----------")    
print("Num of studends :",len(studendsList))

#Q5
print("----------Q5----------")
print(list(map(lambda x:x.printinfo(),Employeelist)))

#Q6
print("----------Q6----------")
print(list(map(lambda x:x.printInfo(),studendsList)))

#Q7
print("----------Q7----------")
hight=0
for u in studendsList:
    if u.getAverage()>hight:
        hight=u.getAverage()
print(hight)

#q8
print("----------Q8----------")
min=Employeelist[0].getMinLon()
for u in Employeelist:
    if len(u.getloans())>0:
        if u.getMinLon()<min:
            min=u.getMinLon()
print(min)

#qQ9
print("----------Q9----------")
max=0
for u in Employeelist:
    if len(u.getloans())>0:
        if u.getMaxLon()>max:
            max=u.getMaxLon()
print(max)
 
#qQ10
print("----------Q10----------")
def Totle(lista):
    grand=0
    for u in lista:
        a=list(u.getloans())
        c=u.getTotalLoans()
        grand=grand+c

        print("getloans: ", a)
        print("getTotalLoans: ",c)
    print( "GrandTotal: ", grand)
Totle(Employeelist)

#Q13
print("----------Q13----------")
for n in studendsList:
    if(len(n.getA())> 0):
        print(n.getName())
        print(n.getSubject())
        print(n.getA())
    print("________")

#Q14
def maxsalary(Employeelist):
    print("----------Q14----------")
    max=0
    for u in Employeelist:
        if u.getSalary()>max:
            max=u.getSalary()
    print(max) 
maxsalary(Employeelist)   

#Q15
def lowsalary(Employeelist):
    print("----------Q15----------")
    min=Employeelist[0].getSalary()
    for u in Employeelist:
        if u.getSalary()<min:
            min=u.getSalary()
    print(min) 
lowsalary(Employeelist) 

#Q16
def Totalsalary(Employeelist):
    print("----------Q16----------")
    total=0
    for u in Employeelist:
        total=total+u.getSalary()
    print(total)
Totalsalary(Employeelist)