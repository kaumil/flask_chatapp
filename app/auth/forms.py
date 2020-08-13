from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_input = StringField('Search for products ',validators=[DataRequired()])
    submit = SubmitField('Search')