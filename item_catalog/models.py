from item_catalog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True)
    email = db.Column(db.String(80), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<user: {self.username}>'


class Catalog(db.Model):

    __tablename__ = 'catalogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    items = db.relationship('Item', backref='catalog', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<catalog {self.name}>'

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'items': self.has_items
        }


class Item(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    catalog_id = db.Column(db.Integer,
                           db.ForeignKey('catalogs.id'), nullable=False)
    creator_id = db.Column(db.String(100))

    def __init__(self, name, description, catalog_id, creator_id):
        self.name = name
        self.description = description
        self.catalog_id = catalog_id
        self.creator_id = creator_id

    def __repr__(self):
        return f'<Item {self.name}>'

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'catalog_id': self.catalog_id
        }
