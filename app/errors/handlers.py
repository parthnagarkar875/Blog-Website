from flask import Blueprint, render_template

errors= Blueprint('errors', __name__)

#There's also a method called errorhandler() but we aren't using it as it would only be applicable for this blueprint. 
#Our main goal is to enable the error handlers throughout the application. 

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404      #404 is specified to give the correct error code response.

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403      #404 is specified to give the correct error code response.

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500      #404 is specified to give the correct error code response.

