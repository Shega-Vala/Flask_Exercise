
from urllib import request
from flask import Flask, render_template, request
import datetime


app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.

studentOrganisationDetails = {
    'John' : 'UNCC',
    'Bill' : 'Carolinas CP',
    'Toni' : 'UFC',
    'Nina' : 'Atrium',
    'Ben'  : 'Lowes'
}


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
    
    # Display "{Number} is even" if given number is even on result.html page
    if  int(number) % 2 == 0:
       display_message=f"{number} is even"
       
    # Display "{Number} is odd" iff given number is odd on result.html page   
    elif int(number) % 2 != 0:
       display_message =f"{number} is odd" 
      
    # Display "No number provided" if value is null or blank on result.html page
    elif (number == " "):
        display_message="No number provided"
    # Display "Provided input is not an integer!" if value is not a number on result.html page       
    elif type(number) != int :
      display_message =  "Provided input is not an integer!"  
    # Write your to code here to check whether number is even or odd and render result.html page

    return render_template('result.html', name=display_message) 
              

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['reg_name']
    studentOrganisations = request.form['org_name']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName]= studentOrganisations
    # Display studentDetails.html with all students and organisations
    
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
