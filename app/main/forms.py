from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,ValidationError,SubmitField
from wtforms.validators import DataRequired
from ..models import Blog

class NewblogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    blog = TextAreaField('Blog', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Add Blog', validators=[DataRequired()])

