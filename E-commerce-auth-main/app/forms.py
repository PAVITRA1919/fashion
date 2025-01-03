from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo

from . import db
from .models import Product
from flask_wtf import FlaskForm
from flask import Blueprint,session,flash,redirect,url_for
from wtforms import StringField, IntegerField, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired, NumberRange
from flask_uploads import IMAGES
from werkzeug.utils import secure_filename

# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
# from flask_reuploaded import UploadSet, configure_uploads, IMAGES

forms = Blueprint('forms', __name__)

# @forms.before_request
# def restrict():
#     if session.get('role') != 'admin':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    role = SelectField('Role', choices=[('customer', 'Customer'), ('delivery_person', 'Delivery Person')], validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')





# a flask form class for new product that is used for creating an html form
class New_Product_Form(FlaskForm):
    name = StringField("Name of Product", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired(), NumberRange(min=1)])
    description = StringField("Product Description", validators=[DataRequired()])
    product_category = StringField("Product Category", validators=[DataRequired()])
    size = StringField("Product Size", validators=[DataRequired()])
    colour = StringField("Color", validators=[DataRequired()])
    quantity = StringField("Product Quantity", validators=[DataRequired()])
    manufacturer = StringField("Product Manufacturer", validators=[DataRequired()])
    country_of_origin = StringField("Country Of Origin", validators=[DataRequired()])
    rating = DecimalField("Rating", validators=[InputRequired(), NumberRange(min=0.0, max=5.0)])
    discount = IntegerField("Discount", validators=[InputRequired(), NumberRange(min=0, max=100)])
    image_url = FileField(
        "Choose a Product Picture",
        validators=[FileRequired(), FileAllowed(IMAGES, message="Please upload an image for Product Picture.")],
    )


