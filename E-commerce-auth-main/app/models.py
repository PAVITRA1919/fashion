from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
# from .__init__ import db
from . import db
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# User table
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    reset_token = db.Column(db.String(128), nullable=True)
    status = db.Column(db.String(20), default='pending')
    
    # Relationships
    cart = db.relationship('Cart', backref='user', lazy=True)
    wishlist = db.relationship('Wishlist', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Product table
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    product_category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    size = db.Column(db.String(20), nullable=True)
    color = db.Column(db.String(20), nullable=True)
    # department = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(100), nullable=True)
    country_of_origin = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    discount = db.Column(db.Float, nullable=True)
    
    # Relationships
    cart_items = db.relationship('Cart', backref='product', lazy=True)
    wishlist_items = db.relationship('Wishlist', backref='product', lazy=True)
    order_items = db.relationship('Order', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Cart table
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cart {self.id}>'

# Wishlist table
class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f'<Wishlist {self.id}>'

#Order table
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    order_amount = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id',ondelete="CASCADE"), nullable=False)
    # status = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Enum('pending', 'shipped', 'delivered','failed'), default='pending')
    payment_method=db.Column(db.String(50), default='Cash_on_delivery')

    # product = relationship("Product", backref="order_items")
    def __repr__(self):
        return f'<Order {self.id}>'


database = SQLAlchemy(model_class=declarative_base())