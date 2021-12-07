import os

# Fallback value in case path isn't defined in the database variables
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Create various configuration options as a class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temporary-alternative-to-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False