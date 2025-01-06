# from flask_login import UserMixin

# from . import db

# from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
# from sqlalchemy.orm import declarative_base, relationship
# from flask_sqlalchemy import SQLAlchemy


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     role = db.Column(db.String(20), nullable=False)
#     contact = db.Column(db.String(20), nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     dob = db.Column(db.Date, nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     reset_token = db.Column(db.String(128), nullable=True)
#     status = db.Column(db.String(20), default='pending')
    
#     def __repr__(self):
#         return f'<User {self.username}>'
    

# # create the db
# db = SQLAlchemy(model_class=declarative_base())


# # # User Table
# # # class User(db.Model):
# # #     __tablename__ = "User"
# # #     User_ID = Column(Integer, primary_key=True)
# # #     Name = Column(String)
# # #     Email = Column(String, unique=True)
# # #     Password = Column(String)
# # #     Role = Column(String)
# # #     Phone_number = Column(String)
# # #     Address = Column(String)
# # #     Gender = Column(String)
# # #     DOB = Column(Date)

# # #     carts = relationship("Cart", back_populates="user")
# # #     wishlists = relationship("Wishlist", back_populates="user")
# # #     orders = relationship("Order", back_populates="user")


# # # Product Table
# # class Product(db.Model):
# #     __tablename__ = "Product"
# #     Product_ID = Column(Integer, primary_key=True)
# #     Name = Column(String)
# #     Price = Column(Float)
# #     Description = Column(String)
# #     Category = Column(String)
# #     Image_URL = Column(String)
# #     Size = Column(String)
# #     Colour = Column(String)
# #     Quantity = Column(Integer)
# #     Manufacturer = Column(String)
# #     Country_of_Origin = Column(String)
# #     Rating = Column(Float)
# #     Discount = Column(Float)

# #     carts = relationship("Cart", back_populates="product")
# #     wishlists = relationship("Wishlist", back_populates="product")
# #     orders = relationship("Order", back_populates="product")


# # # Cart Table
# # class Cart(db.Model):
# #     __tablename__ = "Cart"
# #     Cart_ID = Column(Integer, primary_key=True)
# #     User_ID = Column(Integer, ForeignKey("User.User_ID"))
# #     Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))
# #     Total_Price = Column(Float)
# #     Quantity = Column(Integer)

# #     user = relationship("User", back_populates="carts")
# #     product = relationship("Product", back_populates="carts")


# # # Wishlist Table
# # class Wishlist(db.Model):
# #     __tablename__ = "Wishlist"
# #     Wishlist_ID = Column(Integer, primary_key=True)
# #     User_ID = Column(Integer, ForeignKey("User.User_ID"))
# #     Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))

# #     user = relationship("User", back_populates="wishlists")
# #     product = relationship("Product", back_populates="wishlists")


# # # Order Table
# # class Order(db.Model):
# #     __tablename__ = "Order"
# #     Order_ID = Column(Integer, primary_key=True)
# #     Order_Amount = Column(Float)
# #     Order_Date = Column(Date)
# #     User_ID = Column(Integer, ForeignKey("User.User_ID"))
# #     Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))

# #     user = relationship("User", back_populates="orders")
# #     product = relationship("Product", back_populates="orders")
# #     # tracking_details = relationship("TrackingDetails", back_populates="order")

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
    status = db.Column(db.Enum('pending', 'shipped', 'delivered'), default='pending')
    payment_method=db.Column(db.String(50), default='Cash_on_delivery')

    # product = relationship("Product", backref="order_items")
    def __repr__(self):
        return f'<Order {self.id}>'


database = SQLAlchemy(model_class=declarative_base())