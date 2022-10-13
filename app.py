from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime


app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return render_template('index.html', currentDate=currentDate)
      
@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')
    

@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    global number
    number = request.form['number']
    # Display "Number {Number} is even" if given number is even on result.html page
    if  int(number % 2) == 0:
       display_message="Number {Number}is even"
    # Display "Number {Number} is odd" if given number is odd on result.html page   
    elif int(number % 2) != 0:
       display_message ="Number {Number}is odd" 
    # Display "No number provided" if value is null or blank on result.html page
    elif (number == null):
        display_message="No number provided"
    # Display "Provided input is not an integer!" if value is not a number on result.html page       
    elif type(number) != int :
      display_message =  "Provided input is not an integer!"  
      
      return render_template('result.html', number=number, name=display_message) 
              
   
    # Write your to code here to check whether number is even or odd and render result.html page
    

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
