
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:09:53 2020

@author: Parth
"""

from flask import Flask,redirect,request,render_template,flash,url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 
from app.models import User, Post
from datetime import datetime
from app.forms import RegistrationForm, LoginForm
from app import app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm() 
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)           #if the user checks the remember me box, then it'll be true, else false. 
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Unsuccessful login",'danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))    

@app.route('/account')
@login_required              #Ensures that the user is logged in before accessing the page. 
# =============================================================================
# In the __init__.py file, I have declared a variable login_manager.login_view='login' 
# this basically tells flask to redirect to the login page if the user's trynna access a page 
# that requires him/her to login in the first place.
# =============================================================================
def account():
    return render_template('account.html',title='Account')



    