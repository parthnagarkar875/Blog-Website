# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:42:13 2020

@author: Parth
"""
from app import db, login_manager, app
from flask_login import UserMixin    #This provides default implementations for the methods that Flask-Login expects user objects to have.
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# =============================================================================
# load_user passes id of the user to flask so that it can fetch the appropraite 
# id from the database
# =============================================================================


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file= db.Column(db.String(20),nullable=False, default='default.jpg')    
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)    #Lazy argument defines when the data will be loaded form the database. 
    
    def get_reset_token(self, expires_sec=1800):
# Sample:
# >>>token = s.dumps({'user_id':1}).decode('utf-8')
# >>>token
# 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5MDQyMDE4OSwiZXhwIjoxNTkwNDIwMjE5fQ.eyJ1c2VyX2lkIjoxfQ.cKZspdeU4Z0nWpabZwBc_1YXgIV5VqTsaH5z2u3NQ113N_u9uuTz0l73G_a7mQS-VkZQjDNtw2eTb12pXy5oyw'

        s=Serializer(app.config['SECRET_KEY'], expires_sec)             #Generating a token
        return s.dumps({'user_id': self.id}).decode('utf-8') 

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(app.config['SECRET_KEY'])                          #from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
        try:                                                            
            user_id=s.loads(token)['user_id']                           #s.loads(token) (next line output)= {'user_id': 1}
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):     #__repr__ method is used for returning a printable representation of a python object.        
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
    
class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
