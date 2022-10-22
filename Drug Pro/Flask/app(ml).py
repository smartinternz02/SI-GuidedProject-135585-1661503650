# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:12:54 2022

@author: user
"""
from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open(r"C:/Users/DELL/Desktop/Drug Pro/Flask/model.pkl",'rb'))

app = Flask(__name__)


@app.route("/")
def about():
    return render_template('home.html')



@app.route("/predict")      
def home1():
    return render_template('predict.html')



@app.route("/submit")      
def home2():
    return render_template('submit.html')


if __name__ == "__main__":
 app.run(debug=False)
