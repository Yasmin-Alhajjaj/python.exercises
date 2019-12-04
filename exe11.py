#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:42:25 2019

@author: owner

#Q1
from tkinter import *

def action():
    if enter1.get()=="Orange" and enter2.get()=="CodingAcademy":
        answer = messagebox.showinfo("Login", "Successful login")
        if answer == "ok":
             blog.destroy()
    else:
         messagebox.showinfo("Login", "Wrong User Name or Password")

blog = Tk()
name = Label(blog, text = "Name").grid(row=0, sticky=E)
password = Label(blog, text ="Password").grid(row = 1, sticky=E)
enter1 = StringVar()
enter2 = StringVar()

e1=Entry(blog, textvariable= enter1).grid(row = 0, column = 1)
e2=Entry(blog, textvariable= enter2).grid(row = 1, column = 1)

submit = Button(blog, text="Submit", command= action).grid(row = 3, column = 0)
parent.mainloop()

#Q2

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
def open_child1():
    dialog_title=""
    dialog_text="This is a message"
    answer=messagebox.showinfo(dialog_title,dialog_text)
def open_child2():
    top=Tk()
    top.title('Child window 2')
    top.geometry('400x250')
    name=Label(top,text="Emy Number").place(x=30,y=50)
    email=Label(top,text="Emy Name").place(x=30,y=90)
    e1=Entry(top).place(x=100,y=50)
    e2=Entry(top).place(x=100,y=90)
    button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
    button.pack()
    top.mainloop()
def open_child3():
    win=Tk()
    win.title("Welcome")
    win.geometry('350x200')
    txt=scrolledtext.ScrolledText(win,width=40,height=10)
    txt.grid(column=0,row=0)



root = Tk()
root.title('Root window')
Button(root, text = 'open child window 1', command = open_child1).grid()
Button(root, text = 'open child window 2', command = open_child2).grid()
Button(root, text = 'open child window 3', command = open_child3).grid()
root.mainloop()

"""

# Q3
from tkinter import *
from tkinter.colorchooser import *
root = Tk()
def getcolor():
    color=askcolor()
    root.config(background=color[1])

Button(root,text="select",command=getcolor).pack()
mainloop()















