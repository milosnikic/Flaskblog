from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, DateField, TextAreaField
#wtforms instalirano vec sa pip install flask-wtf          #za proveru jednakosti
from wtforms.validators import DataRequired,Length, Email, EqualTo, ValidationError
from flaskblog.models import User


#DataRequired da polje mora biti popunjeno
#Length za proveru duzine
#Email za pravilan unos mejla
#EqualTo za proveru jednakosti

#Forma za registraciju
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    # gender = RadioField('Gender',choices=[('M','Male'),('F','Female')],validators=[DataRequired()])
    # date = DateField('Date of birth',format='%d-%m-Y')
    password = PasswordField('Password',
                validators=[DataRequired()])
    password_confirmation = PasswordField('Confirm password',
                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please chooose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please chooose a different one')


#Forma za logovanje
class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


#Forma za update
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpeg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please chooose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please chooose a different one')


#Forma za nove postove
class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Enter your content', validators=[DataRequired()])
    submit = SubmitField('Post')