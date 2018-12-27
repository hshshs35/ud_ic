from flask import redirect, url_for, render_template, Blueprint, flash
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import logout_user
from flask import session
import os
# disable HTTPS requirement from flask-dance
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


blueprint = make_google_blueprint(
    client_id='570473588473-lsrlci82153il4lmnlh51jqv4eonb9mc.apps.googleusercontent.com',
    client_secret='A8Ajojm7GyodfLjwVhTohval',
    offline=True, scope=['profile', 'email'])

oauth = Blueprint('oauth', __name__)


@oauth.route('/login/oauth')
def login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    return redirect(url_for('core.index'))


@oauth.route('/logout')
def logout():
    token = blueprint.token['access_token']
    google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    session.clear()
    return redirect(url_for('core.index'))



