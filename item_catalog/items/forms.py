from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms import ValidationError


from flask_login import current_user
from item_catalog.models import Item


class CreateItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    catalog = SelectField('Catalog', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Item')


class EditItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Update Item')