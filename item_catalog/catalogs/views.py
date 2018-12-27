from flask import render_template, url_for, flash, \
                        redirect, request, Blueprint

from item_catalog.models import Item, Catalog
from flask import jsonify
from flask_dance.contrib.google import google

catalogs = Blueprint('catalogs', __name__)


# get the catalog
@catalogs.route('/catalogs/<int:catalog_id>')
def get_catalog(catalog_id):
    catalog = Catalog.query.filter_by(id=catalog_id).first()
    items = Item.query.filter_by(catalog_id=catalog_id).all()
    return render_template('catalog.html', catalog=catalog, items=items, is_login=google.authorized)


# catalog json api
@catalogs.route('/catalogs.json')
def catalog_api():
    res = []
    catalogs = Catalog.query.all()
    for catalog in catalogs:
        cid = catalog.id
        items = Item.query.filter_by(catalog_id=cid).all()
        setattr(catalog,'has_items', [i.serialize for i in items])
        res.append(catalog.serialize)
    return jsonify(Catalog_Items=res)
