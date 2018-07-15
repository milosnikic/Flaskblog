from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField #wtforms instalirano vec sa pip install flask-wtf          #za proveru jednakosti
from wtforms.validators import DataRequired

#DataRequired da polje mora biti popunjeno
#Length za proveru duzine
#Email za pravilan unos mejla
#EqualTo za proveru jednakosti

#Forma za nove postove
class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Enter your content', validators=[DataRequired()])
    submit = SubmitField('Post')