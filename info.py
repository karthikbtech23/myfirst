# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:31:43 2024

@author: KARTHIK S M
"""
from flask import Flask,render_template

app=Flask(__name__)  
@app.route('/')
def show_students():
    students = [
    {"name": "Alice", "age":20},
    {"name": "Bob", "age": 21},
    {"name": "charlie", "age":22},
 ]
    return render_template('info.html', students=students)

app.run(debug=True)
