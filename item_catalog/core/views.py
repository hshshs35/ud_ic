from flask import render_template, request, Blueprint
from item_catalog.models import Catalog

core = Blueprint('core', __name__)


@core.route('/')
def index():
    catalogs = Catalog.query.all()
    return render_template('index.html', catalogs=catalogs)