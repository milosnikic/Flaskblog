from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
#Za generisanje random sifre koristili smo modul secrets
#import secrets
#secrets.token_hex(16) 16 oznacava koliko bajtova zelimoappa
app.config['SECRET_KEY'] = 'd61e93ee0b50a45f2cc5e5dece48bfa1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #function name of route
login_manager.login_message_category = 'info' #class in bootstrap


from flaskblog import routes
