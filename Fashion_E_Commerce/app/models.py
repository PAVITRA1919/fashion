from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy

# create the db
db = SQLAlchemy(model_class=declarative_base())


# User Table
class User(db.Model):
    __tablename__ = "User"
    User_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Email = Column(String, unique=True)
    Password = Column(String)
    Role = Column(String)
    Phone_number = Column(String)
    Address = Column(String)
    Gender = Column(String)
    DOB = Column(Date)

    carts = relationship("Cart", back_populates="user")
    wishlists = relationship("Wishlist", back_populates="user")
    orders = relationship("Order", back_populates="user")


# Product Table
class Product(db.Model):
    __tablename__ = "Product"
    Product_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Float)
    Description = Column(String)
    Category = Column(String)
    Image_URL = Column(String)
    Size = Column(String)
    Colour = Column(String)
    Quantity = Column(Integer)
    Manufacturer = Column(String)
    Country_of_Origin = Column(String)
    Rating = Column(Float)
    Discount = Column(Float)

    carts = relationship("Cart", back_populates="product")
    wishlists = relationship("Wishlist", back_populates="product")
    orders = relationship("Order", back_populates="product")


# Cart Table
class Cart(db.Model):
    __tablename__ = "Cart"
    Cart_ID = Column(Integer, primary_key=True)
    User_ID = Column(Integer, ForeignKey("User.User_ID"))
    Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))
    Total_Price = Column(Float)
    Quantity = Column(Integer)

    user = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")


# Wishlist Table
class Wishlist(db.Model):
    __tablename__ = "Wishlist"
    Wishlist_ID = Column(Integer, primary_key=True)
    User_ID = Column(Integer, ForeignKey("User.User_ID"))
    Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))

    user = relationship("User", back_populates="wishlists")
    product = relationship("Product", back_populates="wishlists")


# Order Table
class Order(db.Model):
    __tablename__ = "Order"
    Order_ID = Column(Integer, primary_key=True)
    Order_Amount = Column(Float)
    Order_Date = Column(Date)
    User_ID = Column(Integer, ForeignKey("User.User_ID"))
    Product_ID = Column(Integer, ForeignKey("Product.Product_ID"))

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    # tracking_details = relationship("TrackingDetails", back_populates="order")


# TrackingDetails Table
# class TrackingDetails(db.Model):
#     __tablename__ = "TrackingDetails"
#     Tracking_ID = Column(Integer, primary_key=True)
#     Status = Column(String)
#     Order_ID = Column(Integer, ForeignKey("Order.Order_ID"))

#     order = relationship("Order", back_populates="tracking_details")
#     # delivery_dashboard = relationship("DeliveryDashboard", back_populates="tracking_details")


# # DeliveryDashboard Table
# class DeliveryDashboard(db.Model):
#     __tablename__ = "DeliveryDashboard"
#     Id = Column(Integer, primary_key=True)
#     Order_ID = Column(Integer, ForeignKey("Order.Order_ID"))
#     Status = Column(String)

    # tracking_details = relationship("TrackingDetails", back_populates="delivery_dashboard")
