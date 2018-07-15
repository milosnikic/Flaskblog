import os

class Config:
    #Za generisanje random sifre koristili smo modul secrets
    #import secrets
    #secrets.token_hex(16) 16 oznacava koliko bajtova zelimoappa
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #Podesavanje varijabli za slanje mejla
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #Ovaj korak zahteva setovanje environment varijabli u odgovarajucem rc fajlu (.bashrc,.bash_profile,.profile)
    #Zato sto koristim zsh (aka zshell) potrebno je u /home/milos/.zshrc fajlu dodati linije
    #export EMAIL_USER="email@koji.treba"
    #export EMAIL_PASS="odgovarajucasifra"
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PAS')
