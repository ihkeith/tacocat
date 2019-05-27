from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)

from models import User

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )


class TacoCreationForm(FlaskForm):
    protein = StringField(
        'Protein',
        validators=[
            DataRequired(),
            Length(max=25),
        ]
    )
    shell = StringField(
        'Shell',
        validators=[
            DataRequired(),
            Length(max=25),
        ]
    )
    cheese = BooleanField(
        'Cheese',
        validators=[
            DataRequired(),
        ]
    )
    extras = StringField(
        'Extras',
        validators=[
            DataRequired(),
            Length(max=25),
        ]
    )
