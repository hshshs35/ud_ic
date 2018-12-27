from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


# error page for 404 error
@errors.app_errorhandler(404)
def handler_404(error):
    return render_template('error_pages/404.html'), 404