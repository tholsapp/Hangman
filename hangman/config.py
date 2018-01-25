
import os
basedir = os.path.abspath(os.path.dirname(__file__))


"""
The configuration settings are defined as class variables
inside the Config class. As the application needs more
configuration items, they can be added to this class, and
later
"""
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or \
      'you-will-never-guess'

  # The Flask-SQLAlchemy extension takes the location of the
  # application's database from the SQLALCHEMY_DATABASE_URI
  # configuration variable
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'app.db')

  # Disable alerts when changes to the database are made
  SQLALCHEMY_TRACK_MODIFICATIONS = False


