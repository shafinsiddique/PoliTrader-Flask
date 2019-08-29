from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    passwordConf = PasswordField('Confirm Password',
                                 validators=[DataRequired(),
                                EqualTo('password')])

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField("Login")



