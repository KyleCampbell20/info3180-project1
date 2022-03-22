from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'md$bV+S*vG9-L'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mfvrdaqykxutvh:e937b9fef2be75a98e19cdcd24cc9b7994e8cd1fb96423958e3a1594cc130a47@ec2-44-194-92-192.compute-1.amazonaws.com:5432/d18dq6eqkos39b'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models