# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:06:56 2020

@author: Parth
"""
import os
from flask_login import LoginManager           #flask_login makes it really easy to manage user sessions. 
from flask import Flask,redirect,render_template,flash,url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from app.config import Config
# =============================================================================
# Tells your Flask application where to look for the files. When using a single module, use __name__ but when using a package, 
# it is better to hardcode the name of the package. 
# =============================================================================
db= SQLAlchemy()
bcrypt=Bcrypt()      #Bcrypt is de-optimized unlike MD5 and SHA1 in order to make it more difficult to get cracked
login_manager=LoginManager()     
login_manager.login_view='users.login'
login_manager.login_message_category='info'
#Below code is for logging in via gmail for the purpose of sending reset email. It has been moved in config.py to enable modularity. 
mail = Mail()


def create_app(config_class=Config):
    app=Flask(__name__) 
    app.config.from_object(Config)      #importing config settings. 
        
    db.init_app(app)
    bcrypt.init_app(app)      #Bcrypt is de-optimized unlike MD5 and SHA1 in order to make it more difficult to get cracked
    login_manager.init_app(app)     
    mail.init_app(app)

    #I've created blueprints in the below modules. Hence, I am using register_blueprints for those modules. 
    from app.users.routes import users
    from app.main.routes import main
    from app.posts.routes import posts
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    return app