# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:06:46 2020

@author: Parth
"""
from app import app

if __name__ == '__main__':
    app.run(debug=True)


'''
Commands used to create database, insert values and print values:
--> from app import db
--> db.create_all()         #This creates the database structure. 
--> from app import User, Post
--> user_1 = User(username='Parth', email='nagarkarparth@gmail.com', password='goat')
--> db.session.add(user_1)
--> db.session.commit()
--> User.query.first()      #Gives the first row stored in the database. 
--> user= user.query.filter_by(username='Parth').first()
--> post_1 = Post(title= 'Blog 1', content='First Post Content', user_id=user.id) 
--> db.session.add(post_1)
--> db.session.commit()
--> user.posts
--> post.author
'''

