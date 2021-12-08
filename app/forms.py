from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """
    Form submitted upon a log in request
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    """
    Form to be filled in by new users
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired()])
    submit = SubmitField('Sign up')