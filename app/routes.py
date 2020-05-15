
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:09:53 2020

@author: Parth
"""

from flask import Flask,redirect,render_template,flash,url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 
from app.models import User, Post
from datetime import datetime
from app.forms import RegistrationForm, LoginForm
from app import app,db, bcrypt

# =============================================================================
# WSGI= Web Server Gateway Interface. 
# It is an interface that allows the servers to send data/requests to the applications for processing.
# =============================================================================
  
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

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
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')         #decode method is used to represent it in a string rather than bytes.
        user=User(username=form.username.data, email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        
        flash(f'Account created for {form.username.data}! You may now login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash("Unsuccessful login",'danger')
    return render_template('login.html',title='Login',form=form)



    