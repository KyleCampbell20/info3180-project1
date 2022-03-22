import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://mfvrdaqykxutvh:e937b9fef2be75a98e19cdcd24cc9b7994e8cd1fb96423958e3a1594cc130a47@ec2-44-194-92-192.compute-1.amazonaws.com:5432/d18dq6eqkos39b').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'app/static/uploads')