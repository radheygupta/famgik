from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, url, email


class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), email()])
    password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
