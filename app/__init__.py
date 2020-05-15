# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:06:56 2020

@author: Parth
"""


from flask import Flask,redirect,render_template,flash,url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# =============================================================================
# Tells your Flask application where to look for the files. When using a single module, use __name__ but when using a package, 
# it is better to hardcode the name of the package. 
# =============================================================================
app=Flask(__name__) 
app.config['SECRET_KEY']= 'e4404166e9d8df572cfa785bafa4cdb7'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)

#Bcrypt is de-optimized unlike MD5 and SHA1 in order to make it more difficult to get cracked


from app import routes

