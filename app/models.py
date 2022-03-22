from turtle import title
from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    numberofbedrooms = db.Column(db.Integer)
    numberofbathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.String(80))
    type = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    photoname = db.Column(db.Text, nullable=False)

    def __init__(self, title, numberofbedrooms, numberofbathrooms, location, price, type, description, photoname ):
        self.title = title
        self.numberofbedrooms = numberofbedrooms
        self.numberofbathrooms = numberofbathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photoname = photoname


