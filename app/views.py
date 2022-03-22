"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os

from turtle import title
from urllib.request import Request
from app import app, db
from flask import flash, render_template, send_from_directory ,request, redirect, url_for
from .propertyform import Propertyform
from werkzeug.utils import secure_filename
from  .models import Property
from operator import length_hint


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def createProperties():
    myform= Propertyform()

    if request.method == 'GET':
        return render_template('propertyform.html', form= myform)

    if request.method =='POST' and myform.validate_on_submit():
            
        photo = myform.photo.data 
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        title = myform.title.data
        numberofbedrooms = myform.numberofbedrooms.data
        numberofbathrooms = myform.numberofbathrooms.data
        location  = myform.location.data
        type= myform.type.data
        price = myform.price.data
        description =  myform.description.data

        propertyvalues = Property(title=title, numberofbedrooms=numberofbedrooms, numberofbathrooms=numberofbathrooms, location=location, type=type, price=price, description=description, photoname= filename )
        db.session.add(propertyvalues)
        db.session.commit()
        

        flash('Property was successfully added')
        return redirect(url_for('displayproperties'))
    else:
            flash('Error, Property was not added')
    flash_errors(myform)
    return render_template('propertyform.html', form=myform)


@app.route('/properties') 
def displayproperties():
    filename = get_uploaded_images()
    if get_propertyinfo() != []:
        subdire = 'uploads/'
        length =length_hint(get_propertyinfo())
        return render_template('properties.html', filenames= filename , propinfo = get_propertyinfo() ,subdire = subdire,len = length)
    else: 
        flash("There are currently no properties in the database")
        return redirect('properties.html')


@app.route('/properties/<int:id>')
def viewproperty(id):
    viewproperty = Property.query.get_or_404(id)
    return render_template('viewproperty.html', viewproperty = viewproperty, rootdire = 'uploads/')
    
@app.route('/properties/create/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), path=filename)

  

def get_uploaded_images():
    rootdir = os.getcwd()
    file_store=[]
    for subdir, dirs, files in os.walk('app/static/uploads'):
        for file in files:
            file_store.append(os.path.join(rootdir,subdir, file))
    return file_store


def get_propertyinfo():
    propertyinfo = Property.query.all()
    return propertyinfo
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
