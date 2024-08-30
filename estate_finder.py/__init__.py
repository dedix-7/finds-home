import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newone.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'your-secret-key'
# app.config['UPLOAD_FOLDER'] = '/Estate_finder/img/'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['MAX_CONTENT_LENGTH'] =  16 *  1024 *  1024  # Limit to  16MB
app.config['STATIC_FOLDER'] = '/estate_finder/static/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'png', 'jpeg'}
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.',  1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from estate_finder import routes
