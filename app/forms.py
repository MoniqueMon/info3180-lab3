from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class MyForm(FlaskForm):
 name = StringField('Name:',validators=[DataRequired()])
 email = StringField('Email Address:',validators=[DataRequired()])
 subject = StringField('Subject:',validators=[DataRequired()])
 text = StringField('Text Area for a Message:',validators=[DataRequired()])