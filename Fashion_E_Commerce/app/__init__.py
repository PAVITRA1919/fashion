from flask import Flask, redirect, url_for
from . import product
from flask_wtf.csrf import CSRFProtect
from .models import db


def create_app():
    # create the app
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    # load configuration settings
    app.config.from_pyfile("config.py")

    # add the product page to the app
    app.register_blueprint(product.product_blueprint)

    # initialize db
    db.init_app(app)

    # create the tables if they dont exist
    with app.app_context():
        db.create_all()
        

    @app.route("/")
    def home():
        # go to the main page of products
        return redirect(url_for("product.show_products"))

    return app


