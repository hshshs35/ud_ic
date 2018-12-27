from flask import render_template, request, Blueprint, session
from item_catalog.models import Catalog
from flask_dance.contrib.google import google
import json

core = Blueprint('core', __name__)


# index page
@core.route('/')
def index():
    catalogs = Catalog.query.all()
    resp = google.get('/oauth2/v2/userinfo')
    if resp.ok:
        content = json.loads(resp.text)
        session['user_id'] = content['id']
    return render_template('index.html', catalogs=catalogs, is_login=google.authorized)