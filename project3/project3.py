#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:47:07 2019

@author: owner
"""

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import * 


   



root=Tk(className='project 3')
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
root.geometry(w)

def added():
    top=Toplevel(root)
  
  
    top.geometry('400x400')
    num=Label(top,text='Number').place(x=30,y=50)
    name=Label(top,text='Name').place(x=30,y=90)
    gender=Label(top,text='Gender').place(x=30,y=130)
    national=Label(top,text='Nationality').place(x=30,y=170)
    date=Label(top,text='Date of birth').place(x=30,y=210)
    addres=Label(top,text='Address').place(x=30,y=250)
    depart=Label(top,text='Derpart').place(x=30,y=290)
    salary=Label(top,text='Salary').place(x=30,y=330)
    se=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=StringVar()
    val6=StringVar()
    val7=StringVar()
    val8=DoubleVar()
    e1=Entry(top,textvariable=se).place(x=99,y=50)
   
    e2=Entry(top,textvariable=val2).place(x=99,y=90)
  
    e3=Entry(top,textvariable=val3).place(x=99,y=130)
   
    e4=Entry(top,textvariable=val4).place(x=99,y=170)
   
    e5=Entry(top,textvariable=val5).place(x=99,y=210)
  
    e6=Entry(top,textvariable=val6).place(x=99,y=250)
 
    e7=Entry(top,textvariable=val7).place(x=99,y=290)
    e8=Entry(top,textvariable=val8).place(x=99,y=330)
    def act():
        import sqlite3
        conn = sqlite3.connect('OrgDB.db')
        c = conn.cursor()
# =============================================================================
#         c.execute("INSERT INTO OrgDB VALUES (%d,'%s','male',%s,'05/23/1995','amman-jordan','coding',400)" )
# =============================================================================
        c.execute("INSERT INTO OrgDB VALUES (%d,'%s','%s','%s','%s','%s','%s','%f')" %(se.get(),val2.get(),val3.get(),val4.get(),val5.get(),val6.get() ,val7.get(),val8.get()) )
        conn.commit()

        conn.close()
        print( ("INSERT INTO OrgDB VALUES (%d,'%s','%s','%s','%s','%s','%s','%f')" %(se.get(),val2.get(),val3.get(),val4.get(),val5.get(),val6.get() ,val7.get(),val8.get()) ))
        
        messagebox.showinfo('proof','successful add')
    sumbit=Button(top,text='Add',command=act).grid(pady=370,padx=160)

    top.mainloop()
    
    
    
def view():
    txp=Toplevel(root)
    txp.geometry('400x400')
   
    import sqlite3
    txt=scrolledtext.ScrolledText(txp,width=40,height=10)
    conn = sqlite3.connect('OrgDB.db')
    
    c = conn.cursor()
    txt=scrolledtext.ScrolledText(txp,width=40,height=10,wrap=WORD)
    txt.grid(column=0,row=1)
    for row in c.execute('SELECT * FROM OrgDB '):
        txt.insert(END, "number "+ str(row[0]) + "\n")
        txt.insert(END, "Name: "+ str(row[1]) + "\n")
        txt.insert(END, "----- "+  "\n")
#Pushes the scrollbar and focus of text to the end of the text input.
        txt.yview(END)
        txt.pack()

    conn.commit()
   
       
        
        
     
    conn.close()    
# =============================================================================
#     num=Label(txp,text='Number').place(x=30,y=50)
#     name=Label(txp,text='Name').place(x=30,y=90)
#     gender=Label(txp,text='Gender').place(x=30,y=130)
#     national=Label(txp,text='Nationality').place(x=30,y=170)
#     date=Label(txp,text='Date of birth').place(x=30,y=210)
#     addres=Label(txp,text='Address').place(x=30,y=250)
#     depart=Label(txp,text='Derpart').place(x=30,y=290)
#     salary=Label(txp,text='Salary').place(x=30,y=330)
# =============================================================================
    def clo():
        txp.destroy()
    
    sumbit=Button(txp,text='clx',command=clo).grid(pady=370,padx=160)
    txp.mainloop()
    

label=Label(root,text='employee',font=('times',20,'bold'))
label.pack()
b=Button(root,text='add employee',command=added)
b.pack()
b1=Button(root,text='view employee',command=view)
b1.pack()
root.mainloop()


# =============================================================================
# import sqlite3
# conn = sqlite3.connect('OrgDB.db')
# c = conn.cursor()
# num=3
# for row in c.execute('SELECT * FROM OrgDB'):
#     print (row)
# conn.close()
# =============================================================================