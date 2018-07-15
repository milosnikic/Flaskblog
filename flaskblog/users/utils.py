import os
import secrets
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #_ uzimamo za promenljivu koju ne zelimo da koristimo
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn) # odredjivanje putanje slike, gde ce se nalaziti, join omogucava da se to lepo odradi

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn


#Za slanje mejla funkcija
def send_reset_email(user):
    token = user.get_reset_token()
    #kreiranje mejla
    msg = Message('Password Reset Request',
                    sender='noreply@demo.com',
                    recipients=[user.email])
    #_external=True absolute URL
    #Potrebno je skroz levo string pomeriti kako se ne bi tabovi prikazivali
    msg.body = f'''To reset your password visit the following link:
{url_for('users.reset_token',token=token,_external=True)}


If you did not make this request then simply ignore this email and no changes will be made.
'''

    mail.send(msg)
