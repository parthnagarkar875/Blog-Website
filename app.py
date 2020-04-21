# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:06:46 2020

@author: Parth
"""


from flask import Flask

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
def hello():
    return "<h4>Homepage, World!<h4>"

@app.route('/about')
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__':
    app.run(debug=True)

