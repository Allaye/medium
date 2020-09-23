from wtforms import (StringField, SubmitField, PasswordField)
from flask_wtf import FlaskForm
from wtforms.validators import (DataRequired, Email, EqualTo)
from wtforms import ValidationError
from project_login.models import User




class Login(FlaskForm):
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Login')




class Registeration(FlaskForm):

    username = StringField('Enter user name', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    passwrd = PasswordField('Enter passpharse', validators=[DataRequired(), EqualTo('confirmed_password', 'unmatch password please check')])
    confirmed_password = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    


    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken, try another email')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken, try another one')

        
    
    
            