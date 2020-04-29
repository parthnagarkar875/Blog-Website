# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:06:46 2020

@author: Parth
"""

from flask import Flask,redirect,render_template,flash,url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 
from forms import RegistrationForm, LoginForm

posts=[
       {
        'author':'Parth Nagarkar',
        'title':'Blog post 1',
        'content': 'First post content',
        'date_posted':'April 28, 2020'
        },
       {
        'author':'Kamal Chachad',
        'title':'Blog post 2',
        'content': 'Second post content',
        'date_posted':'June 15, 2020'
        }
       ]

# =============================================================================
# Tells your Flask application where to look for the files. When using a single module, use __name__ but when using a package, 
# it is better to hardcode the name of the package. 
# =============================================================================
app=Flask(__name__) 
app.config['SECRET_KEY']= 'e4404166e9d8df572cfa785bafa4cdb7'

# =============================================================================
# WSGI= Web Server Gateway Interface. 
# It is an interface that allows the servers to send data/requests to the applications for processing.
# =============================================================================

@app.route('/')     #Tells the flask app which URL should call the associated function. (Function= home in this case)
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form=LoginForm() 
    return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)

