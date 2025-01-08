from flask import Blueprint, render_template, url_for, redirect, request, flash, current_app, send_from_directory, session
from .forms import New_Product_Form
from .models import db, Product,Order
from werkzeug.utils import secure_filename
import os
from .utils import restrict_to_admin

product = Blueprint("product", __name__, url_prefix="/product")

# @product.before_request
# @restrict_to_admin()
# def restrict_to_admin():
#     if session.get('role') != 'admin':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))


@product.route("/", methods=["GET"])
@restrict_to_admin()
def show_products():
    all_products = db.session.query(Product).all()
    return render_template("all_products.html", products=all_products)


@product.route("/forms", methods=["GET", "POST"])
@restrict_to_admin()
def create_new_product():
    form = New_Product_Form()

    if form.validate_on_submit():
        # Create a new product object
        new_product = Product()
        form.populate_obj(new_product)

        # Handle image upload
        image = form.image_url.data
        if image and image.filename != '':
            image_filename = secure_filename(image.filename)
            upload_path = os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename)
            image.save(upload_path)
            new_product.image_url = f"media/{image_filename}"

        try:
            db.session.add(new_product)
            db.session.commit()
            flash("Product Created Successfully.", "success")
            return redirect(url_for("product.show_products"))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while creating the product: {e}", "danger")

    return render_template("ProductForm.html", form=form, operation_name="Add")


@product.route("/update/<int:product_id>", methods=["GET", "POST"])
@restrict_to_admin()
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = New_Product_Form(obj=product)

    if form.validate_on_submit():
        form.populate_obj(product)  # Populate the existing product object

        # Handle image upload (if a new image is provided)
        image = form.image_url.data
        if image and image.filename != '':
            image_filename = secure_filename(image.filename)
            upload_path = os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename)
            image.save(upload_path)
            product.image_url = f"media/{image_filename}"  # Update image URL

        try:
            db.session.commit()
            flash("Product Updated Successfully.", "success")
            return redirect(url_for("product.show_products"))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while updating the product: {e}", "danger")

    return render_template("ProductForm.html", form=form, operation_name="Update")

# @product.route("/delete/<int:product_id>")
# def delete_product(product_id):
#     product = Product.query.get(product_id)
#     db.session.delete(product)
#     db.session.commit()
#     return redirect(url_for("product.show_products"))

@product.route("/delete/<int:product_id>")
@restrict_to_admin()
def delete_product(product_id):
    # print("delete")
    product = Product.query.get_or_404(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        flash("Product Deleted Successfully.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred while deleting the product: {e}", "danger")

    return redirect(url_for("product.show_products"))


@product.route("/upload/<image_filename>")
@restrict_to_admin()
def get_image(image_filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], image_filename)




