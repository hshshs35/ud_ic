from flask import render_template, url_for, flash, \
                        redirect, request, Blueprint

from flask_login import login_required
from item_catalog import db
from item_catalog.models import Item, Catalog
from item_catalog.items.forms import CreateItemForm, EditItemForm

items = Blueprint('items', __name__)


# get the item
@items.route('/items/<int:item_id>')
def get_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    return render_template('item.html', item=item)


#create the item
@items.route('/items/new', methods=['GET', 'POST'])
@login_required
def create_item():
    form = CreateItemForm()
    form.catalog.choices = [(c.id, c.name) for c in Catalog.query.order_by('name')]

    if form.validate_on_submit():
        catalog_id = form.catalog.data
        item = Item(name=form.name.data,
                    description=form.description.data,
                    catalog_id=catalog_id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('catalogs.get_catalog', catalog_id=item.catalog_id))
    else:
        form.process()
        return render_template('create_item.html', form=form)


# edit the item
@items.route('/items/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):

    item = Item.query.filter_by(id=item_id).first()

    form = EditItemForm()
    form.name.default = item.name
    form.description.default = item.description

    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('items.get_item', item_id=item_id))
    else:
        form.process()
        return render_template('edit_item.html', form=form)


# delete the item
@items.route('/items/<int:item_id>/delete')
@login_required
def delete_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    if item is None:
        return redirect(url_for('core.index'))
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('catalogs.get_catalog', catalog_id=item.catalog_id))
