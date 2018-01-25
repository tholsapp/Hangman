
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

hangman_app = Flask(__name__)
hangman_app.config.from_object(Config)
db = SQLAlchemy(hangman_app)
migrate = Migrate(hangman_app, db)
login = LoginManager(hangman_app)
login.login_view = 'login'

from hangman import routes, models