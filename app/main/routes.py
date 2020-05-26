from flask import render_template, request, Blueprint
from app.models import Post

main= Blueprint('main', __name__)

# =============================================================================
# WSGI= Web Server Gateway Interface. 
# It is an interface that allows the servers to send data/requests to the mainlications for processing.
# =============================================================================
  
@main.route('/')     #Tells the flask main which URL should call the associated function. (Function= home in this case)
@main.route('/home')     
def home():
    page=request.args.get('page', 1, type=int)                #Checking query parameter in URL to display posts
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html',title='About')
