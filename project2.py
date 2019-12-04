#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:10:24 2019

@author: owner


from tkinter import *
root = Tk()
root.title('menu_win')
def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')
top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_command(label='New...', command=notdone)
file.add_command(label='Open...', command=notdone)
file.add_separator()
file.add_command(label='Quit', command=root.destroy)
top.add_cascade(label='File', menu=file)
edit = Menu(top,tearoff= 0)
edit.add_command(label='Cut', command=notdone)
edit.add_command(label='Paste', command=notdone)
top.add_cascade(label='Edit', menu=edit)
root.mainloop()
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
        self.__Marks =dict(marks)    
    def getSubject( self ):
        return "Subject : " + self.__Subject
    def setSubject( self,newsub ):
        return "newSubject : " + self.__Subject   
    def getMarks( self ):
        return "Marks : " , self.__Marks
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

'''
Employee1=Employee(1000,"Ahmad Yazaan","Amman Jordan",500,"HR Consultant",[434,200,1020])
Employee2= Employee(2000,"Hala rana","Aqaba jordan", 750,"Manager",[150,3000,250])
Employee3= Employee(3000,"Mariam ali","Mafraq jordan", 600,"HR s",[304,1000,250,300,500,235])
Employee4= Employee(4000,"Yasmin mohameed","Karak jordan", 865,"Director",[])

Student1=Student(20191000,"Khalid Ali","Irbid Jordan", "History",{"English":80,"Arabic":90,"Art":95,"Management":75})
Student2=Student(20182000,"Reem Hani","Zarqa Jordan", "Softwere Eng",{"English":80,"Arabic":90,"Management":75,"Calculus":85,"OS":73,"Priogramming":90})
Student3=Student(20161001,"Nawras Abdallah","Amman Jordan", "Arts",{"English":83,"Arabic":92,"Art":90,"Management":70})
Student4=Student(20172030,"Amal Raed","Tafelah Jordan", "Computer Eng",{"English":83,"Arabic":92,"Management":70,"Calculus":80,"OS":79,"Priogramming":91})
'''
empl_list = []

from tkinter import *
from tkinter import messagebox

root = Tk(className="My project2")
root.geometry('500x500+500+100')
top = Menu(root)
root.config(menu=top)

def open_about():
    messagebox.showinfo('About Us', 'Made by yasmin & omaima & haya')

def open_reports():
    c = Toplevel(root)
    c.title("Reports")
    c.geometry("500x500+510+230")
    Label(c, text="Reports").grid()






def add_employee():
    value1 = IntVar()
    value2 = StringVar()
    value3 = StringVar()
    value4 = IntVar()
    value5 = IntVar()
    value6 = StringVar()
    
    c = Toplevel(root)
    c.title("Add New Employee")
    c.geometry("500x500+510+230")
    #Label(c, text="Add New Employee").grid()
    Number = Label(c, text = "Number").grid(row = 0, sticky=E)
    e1 = Entry(c, textvariable= value1).grid(row = 0, column =1)
    Name= Label(c, text ="Name").grid(row = 1, sticky=E)
    e2 = Entry(c, textvariable= value2).grid(row = 1, column =1)
    job = Label(c, text = "job").grid(row=2, sticky=E)
    e3 = Entry(c, textvariable= value3).grid(row = 2, column =1)
    salary= Label(c, text ="salary").grid(row = 3, sticky=E)
    e4 = Entry(c, textvariable= value4).grid(row = 3, column =1)
    loans= Label(c, text ="loans").grid(row = 4, sticky=E)
    e5 = Entry(c, textvariable= value5).grid(row = 4, column =1)
    address= Label(c, text ="address").grid(row = 5, sticky=E)
    e6 = Entry(c, textvariable= value6).grid(row = 5, column =1)
    def add():
        #print()
        # lista.append(value1.get())
        #lista.append(value2.get())
        #lista.append(value3.get())
        #lista.append(value4.get())
        #lista.append(value5.get())
        # lista.append(value6.get())
        # print(lista) 
        E1=Employee(value1.get(),value2.get(),value6.get(),value4.get(),value3.get(),[1,5,9])
        #print(Employee1.printinfo())
        empl_list.append(E1)


    save = Button(c, text="save", command= add).grid(row = 7, column = 1)
        #c.mainloop()
    

        #parent = Tk()
#print('rrr',empl_list)    
    
    
   
    
    
    

def view_employee():
    c = Toplevel(root)
    c.title("View Employee")
    c.geometry("500x500+510+230")
    Label(c, text="View Employee").grid()
    for Emp in empl_list:
        data = f"Name: {Emp.getName()} \t" \
               f"Address: {Emp.getAddress()} \t" \
               f"Number: {Emp.Employee_Num} \t" \
               f"Title: {Emp.getJobTitle()} \t" \
               f"Salary: {Emp.getSalary()} \t" \
               f"Loans: {Emp.getloans()} \t" \
               f""
        Label(c, text=data).grid()


def delete_employee():
    c = Toplevel(root)
    c.title("Delete Employee")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Employee").grid()
    valudel=IntVar()
    Number = Label(c, text = "Enter Number").grid(row = 2,column =3)
    
    
    def destro():
     for e,emp in enumerate(empl_list):
        if valudel.get()==emp.Employee_Num:
            empl_list.remove(emp)
            messagebox.showinfo("messagebox", "the employee  Number is delete ")
        #messagebox.showinfo("messagebox", "the employee with this Number doesn't exist")
    de = Entry(c, textvariable= valudel).grid(row = 5, column =3)
    delete = Button(c, text="delete", command= destro).grid(row = 7, column = 1)

    
    
    
stu_list=[]   
def add_student():
    c = Toplevel(root)
    c.title("Add New Student")
    c.geometry("500x500+510+230")
    value1 = IntVar()
    value2 = StringVar()
    value3 = StringVar()
    value4 = StringVar()
    value5 = IntVar()
    
    Number = Label(c, text = "Number").grid(row = 0, sticky=E)
    ea1 = Entry(c, textvariable= value1).grid(row = 0, column =1)
    Name= Label(c, text ="Name").grid(row = 1, sticky=E)
    ea2 = Entry(c, textvariable= value2).grid(row = 1, column =1)
    address= Label(c, text ="address").grid(row = 2, sticky=E)
    ea3 = Entry(c, textvariable= value3).grid(row = 2, column =1)
    Subject = Label(c, text = "Subject").grid(row=3, sticky=E)
    ea4 = Entry(c, textvariable= value4).grid(row = 3, column =1)
    Marks= Label(c, text ="Marks").grid(row = 4, sticky=E)
    ea5 = Entry(c, textvariable= value5).grid(row = 4, column =1)

    
    def addS():
        #print()
        # lista.append(value1.get())
        #lista.append(value2.get())
        #lista.append(value3.get())
        #lista.append(value4.get())
        #lista.append(value5.get())
        # lista.append(value6.get())
        # print(lista) 
        S1=Student(value1.get(),value2.get(),value3.get(),value4.get(),{"English":80,"Arabic":90,"Art":95,"Management":75})
        #print(Employee1.printinfo())
        stu_list.append(S1)


    save = Button(c, text="save", command= addS).grid(row = 7, column = 1)
    
def view_student():
    c = Toplevel(root)
    c.title("View Student")
    c.geometry("500x500+510+230")
    Label(c, text="View Student").grid()
    for Stu in stu_list:
        data = f"Name: {Stu.getName()} \t" \
               f"Address: {Stu.getAddress()} \t" \
               f"Number: {Stu.Student_Num} \t" \
               f"Subject: {Stu.getSubject()} \t" \
               f"marks: {Stu.getMarks()} \t" \
               f""
        Label(c, text=data).grid()

def delete_student():
    c = Toplevel(root)
    c.title("Delete Student")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Student").grid()
    valudel=IntVar()
    Number = Label(c, text = "Enter Number").grid(row = 2,column =3)
    
    
    def destroS():
        for stu in stu_list:
            if valudel.get()==stu.Student_Num:
                stu_list.remove(stu)
                messagebox.showinfo("messagebox", "the employee  Number is delete ")
        #messagebox.showinfo("messagebox", "the employee with this Number doesn't exist")
    de = Entry(c, textvariable= valudel).grid(row = 3, column =3)
    deletes = Button(c, text="delete", command= destroS).grid(row = 5, column = 1)
    


def exit():
    root.destroy()



file = Menu(top, tearoff=0)
file.add_command(label="Reports", command=open_reports)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label="File", menu=file)
employees = Menu(top, tearoff=0)
employees.add_command(label='Add', command=add_employee)
employees.add_command(label='View', command=view_employee)
employees.add_command(label="Delete", command=delete_employee)
top.add_cascade(label="Employees", menu=employees)
students = Menu(top, tearoff=0)
students.add_command(label="Add", command=add_student)
students.add_command(label="View", command=view_student)
students.add_command(label="Delete", command=delete_student)
top.add_cascade(label="Students", menu=students)
help_menu = Menu(top, tearoff=0)
help_menu.add_command(label='About', command=open_about)
top.add_cascade(label="Help", menu=help_menu)
root.mainloop()
#print('rrr',empl_list)    
