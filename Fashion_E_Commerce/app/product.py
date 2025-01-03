from flask import Blueprint, render_template, url_for, redirect, request, flash, current_app, send_from_directory
from .forms import New_Product_Form
from .models import db, Product
from werkzeug.utils import secure_filename
import os

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/")
def show_products():
    all_products = db.session.query(Product).all()
    return render_template("all_products.html", products=all_products)


@product_blueprint.route("/new", methods=["GET", "POST"])
def create_new_product():
    form = New_Product_Form()

    # if the form is being submitted, validate it
    if request.method == "POST":
        if form.validate():
            new_product = Product()
            form.populate_obj(new_product)

            image = form.photo.data
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename))
            new_product.Image_URL = image_filename

            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for("product.show_products"))
        else:
            return form.errors

    # if the form is being asked for, render and return it
    return render_template("new_product_form.html", form=form, operation_name="Add")


@product_blueprint.route("/update/<int:product_id>", methods=["GET", "POST"])
def update_product(product_id):
    product = Product.query.get(product_id)
    form = New_Product_Form(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)

        image = form.photo.data
        image_filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename))
        product.Image_URL = image_filename

        db.session.commit()
        flash("Product Updated Successfully.")
        return redirect(url_for("product.show_products"))
    return render_template("new_product_form.html", form=form, operation_name="Update")


@product_blueprint.route("/delete/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("product.show_products"))


@product_blueprint.route("/upload/<image_filename>")
def get_image(image_filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], image_filename)
