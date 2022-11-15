# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

#HOME--PAGE
@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/")
def add():
    return render_template("home.html")


#SIGN--UP--OR--REGISTER
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/register')
def register():
    return render_template('login.html')
    
#LOGIN--PAGE
    
@app.route("/signin")
def signin():
    return render_template("login.html")
        
@app.route('/login')
def login():
    return render_template('homepage.html')


#ADDING----DATA


@app.route("/add")
def adding():
    return render_template('add.html')


@app.route('/addexpense')
def addexpense():
     return render_template("homepage.html")

#DISPLAY---graph 

@app.route("/display")
def display():       
    return render_template('display.html')
                           
            
 #limit
@app.route("/limit" )
def limit():
       return render_template('/limit.html')


@app.route("/limitnum")
def limitnum():
      return render_template("homepage.html")
     
#REPORT

@app.route("/today")
def today():
    return render_template("today.html" )
     

@app.route("/month")
def month():
    return render_template("month.html")
         
@app.route("/year")
def year():
    return render_template("year.html" )        

if __name__ == "__main__":
    app.run(debug=True)