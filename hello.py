# -*- coding: utf-8 -*-
"""
Created on Fri May 28 08:20:50 2021

@author: ssc
"""


#importing the libraries
#import flask library 
from flask import Flask,request,render_template
import requests
#import regular expression package
import re
#import numpy
import numpy as np
#Defining the app
app = Flask(__name__)


#Defining the Output Function
def check(output):
   url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
   querystring = {"image_url":output,"sourceType" :"url"}
   
   payload = '''{\r\n   \"image_url\": "'''+output+'''",\r\n   \"sourceType\": \"url\"\r\n}'''
   headers ={
           'x-rapidapi-key' : "1d7a71d247msh972960a5666b2a0p15d8bajsnd8200667b29a",
        'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
        }
   response = requests.request("POST",url,headers=headers,params=querystring)

   print(response.text)
   return response.json()["results"][0]["plate"],response.json()["results"][0]["confidence"]

#Routing the html page
#home page
@app.route('/')
def home():
    return render_template('base.html')


#Define Predict function
@app.route('/predict',methods =['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+"with confidence score: "+str(round(conf))+"%")
    
if __name__=="__main__":
   app.run(debug=True)