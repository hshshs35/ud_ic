from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def handler_404(error):
    return render_template('error_pages/404.html'), 404


@errors.app_errorhandler(403)
def handler_403(error):
    return render_template('error_pages/403.html'), 403