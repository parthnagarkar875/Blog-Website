# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:06:46 2020

@author: Parth
"""


from flask import Flask, render_template, url_for     #url_for is used for routing through links. We have used it while linking the CSS file. 

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
app.secret_key= 'parth'

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


if __name__ == '__main__':
    app.run(debug=True)

