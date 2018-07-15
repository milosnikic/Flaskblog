from flask import Blueprint, render_template, url_for
import logging

#
#
#       NEOPHODNA KONFIGURACIJA LOGGERA
#
#

#Kreiranje putanje za cuvanje logga
PATH = '/home/milos/Desktop/python_projects/Flask/flaskblog/logg/errors.log'

#Kreiranje loggera
logger = logging.getLogger(__name__)
#Kreiranje FileHandlera za logger
file_handler = logging.FileHandler(PATH)
#Kreiranje formata za logger
formatter = logging.Formatter("%(asctime)s:%(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
#Podesvanje nivoa logovanja
file_handler.setLevel(logging.ERROR)
#Dodavanje hendlera
logger.addHandler(file_handler)


#Da bismo napravili Blueprint direktorijum mora da bude package
# tj. mora da ima __init__.py fajl

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    logger.error("Page not found")
    return render_template('errors/404.html'), 404 #default je 200, ali je ovde neophodno naznaciti

@errors.app_errorhandler(403)
def error_403(error):
    logger.error("User access denied")
    return render_template('errors/403.html'), 403 #default je 200, ali je ovde neophodno naznaciti

@errors.app_errorhandler(500)
def error_500(error):
    logger.error("Server internal error")
    return render_template('errors/500.html'), 500 #default je 200, ali je ovde neophodno naznaciti
