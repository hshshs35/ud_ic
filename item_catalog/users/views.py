from flask import render_template, url_for, flash, \
                        redirect, request, Blueprint

from flask_login import login_user, current_user, logout_user, login_required
from item_catalog import db
from item_catalog.models import User, Item
from item_catalog.users.forms import SignUpForm, LoginForm

users = Blueprint('users', __name__)


# sign up
@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('signup.html', form=form)


# login
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('succefully logged in')

            next_uri = request.args.get('next')

            if not next_uri:
                next_uri = url_for('core.index')

            return redirect(next_uri)

    return render_template('login.html', form=form)



# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


