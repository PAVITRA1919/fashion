from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask App
app = Flask(__name__)

# db Configuration
app.config['SQLALCHEMY_db_URI'] = 'sqlite:///ecommerce2.db'  # db file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Tables
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100))

class DeliveryPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    status = db.Column(db.String(20))  # Active, Pending, etc.

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Place = db.Column(db.String, nullable=False)
    Payment_Mode = db.Column(db.String (255), nullable=False)
    status = db.Column(db.String(20)) 
    

# Create db and Tables
with app.app_context():
    db.create_all()  # This creates the db and tables

print("db and tables created successfully!")
