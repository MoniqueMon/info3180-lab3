from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'e0180a9b2e32c7'
app.config['MAIL_PASSWORD'] = 'daa0db5b4b9023'
mail = Mail(app)
from app import views