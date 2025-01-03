from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired, NumberRange
from flask_uploads import IMAGES


# a flask form class for new product that is used for creating an html form
class New_Product_Form(FlaskForm):
    Name = StringField("Name of Product", validators=[DataRequired()])
    Price = IntegerField("Price", validators=[DataRequired(), NumberRange(min=1)])
    Description = StringField("Product Description", validators=[DataRequired()])
    Category = StringField("Product Category", validators=[DataRequired()])
    Size = StringField("Product Size", validators=[DataRequired()])
    Colour = StringField("Color", validators=[DataRequired()])
    Quantity = StringField("Product Quantity", validators=[DataRequired()])
    Manufacturer = StringField("Product Manufacturer", validators=[DataRequired()])
    Country_of_Origin = StringField("Country Of Origin", validators=[DataRequired()])
    Rating = DecimalField("Rating", validators=[InputRequired(), NumberRange(min=0.0, max=5.0)])
    Discount = IntegerField("Discount", validators=[InputRequired(), NumberRange(min=0, max=100)])
    photo = FileField(
        "Choose a Product Picture",
        validators=[FileRequired(), FileAllowed(IMAGES, message="Please upload an image for Product Picture.")],
    )
