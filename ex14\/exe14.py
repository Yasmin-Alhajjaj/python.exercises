#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:42:58 2019

@author: owner
"""
"""
#Q1
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the Index page'



@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/Members')
def world():
    return 'Members Page'
    

if __name__=='__main__':
    app.run() 
    
"""    
    
    
#Q2

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/index/<int:u>')
def hello(u):
    return render_template('index.html',score = u)

    
if __name__=='__main__':
    app.run() 
"""      
    
#Q3

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/index')
def Q3():
    return render_template('index2.html')


if __name__=='__main__':
    app.run()

    
""" 
    
    