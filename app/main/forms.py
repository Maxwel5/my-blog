from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import Required
from ..models import User
from wtforms import ValidationError

class NewblogForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    blog = TextAreaField('Blog', [validators.DataRequired()])
    author = StringField('Author', [validators.DataRequired()])

    