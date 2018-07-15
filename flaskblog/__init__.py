from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
import logging

#
#
#       NEOPHODNA KONFIGURACIJA LOGGERA
#
#

#Kreiranje putanje za cuvanje logga
PATH = '/home/milos/Desktop/python_projects/Flask/flaskblog/logs/init.log'

#Kreiranje loggera
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#Kreiranje FileHandlera za logger
file_handler = logging.FileHandler(PATH)
#Kreiranje formata za logger
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)
#Dodavanje hendlera
logger.addHandler(file_handler)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #function name of route
login_manager.login_message_category = 'info' #class in bootstrap
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    #Prebacili smo sve u klasu Config kako bismo lakse mogli da pravimo instance i za testiranje
    app.config.from_object(Config)
    logging.info("App is created.")

    db.init_app(app)
    logging.info("Database is initialized.")
    bcrypt.init_app(app)
    login_manager.init_app(app)
    logging.info("Login manager is initialized.")
    mail.init_app(app)
    logging.info("Mail is initialized.")

    from flaskblog.users.routes import users #users je ime promenljive instance klase Blueprint
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    logging.info("Users blueprint created.")
    app.register_blueprint(posts)
    logging.info("Posts blueprint created.")
    app.register_blueprint(main)
    logging.info("Main blueprint created.")
    app.register_blueprint(errors)
    logging.info("Errors blueprint created.")

    return app
