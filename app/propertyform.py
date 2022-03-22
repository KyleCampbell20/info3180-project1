from random import choices
import string
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, Length


class Propertyform(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    numberofbedrooms= StringField('No. of Bedrooms', validators=[DataRequired()])
    numberofbathrooms= StringField('No. of Bathrooms', validators=[DataRequired()])
    location= StringField('Loacation', validators=[DataRequired()])
    price= FloatField('Price', validators=[DataRequired()])
    type = StringField('Property Type', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=800)])
    house_choices=[('House'), ('Apartment')]
    type= SelectField('Type', choices=house_choices)

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'Images only!'])
    ])


