from item_catalog import db
from item_catalog.models import Catalog

for i in range(10):
    c = Catalog(name='C{}'.format(i+1), description='nothing but a category')
    db.session.add(c)

db.session.commit()