from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

# create the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'item_catalog_secret_2718'

# set up the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'item_catalog.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# set up the login config
# local login and signup are not used anymore since the app switched to the oauth login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# import blueprints
from item_catalog.core.views import core
from item_catalog.users.oauth_views import blueprint
from item_catalog.users.oauth_views import oauth
from item_catalog.items.views import items
from item_catalog.catalogs.views import catalogs
from item_catalog.errors.error_handler import errors

# register routes
app.register_blueprint(errors)
app.register_blueprint(core)
app.register_blueprint(items)
app.register_blueprint(catalogs)
app.register_blueprint(blueprint, url_prefix='/login')
app.register_blueprint(oauth)

