from flask import Blueprint, render_template, url_for, redirect, request, flash, current_app, send_from_directory,session
from .forms import New_Product_Form
from .models import db, Product
from werkzeug.utils import secure_filename
import os
from .utils import restrict_to_admin


product = Blueprint("product", __name__, url_prefix="/product")

# @product.before_request
# @restrict_to_admin 
# def restrict():
#     if session.get('role') != 'admin':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))
    

@product.route("/")
def show_products():
    all_products = db.session.query(Product).all()
    return render_template("all_products.html", products=all_products)


@product.route("/forms", methods=["GET", "POST"])
def create_new_product():
    form = New_Product_Form()

    # if the form is being submitted, validate it
    if request.method == "POST":
        if form.validate():
            # new_product=Product()
            new_product = Product(
                name=form.name.data,
                price=form.price.data,
                description=form.description.data,
                product_category=form.product_category.data,
                # image_url=form.image_url.data,
                size=form.size.data,
                color=form.colour.data,
                quantity=form.quantity.data,
                manufacturer=form.manufacturer.data,
                country_of_origin=form.country_of_origin.data,
                rating=form.rating.data,
                discount=form.discount.data

            )
            form.populate_obj(new_product)

            # image = form.image_url.data
            # image_filename = secure_filename(image.filename)
            # image.save(os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename))
            # new_product.Image_URL = image_filename
            # if image and image.filename != '':
            # Create a safe file path

            image = form.image_url.data  # This is the uploaded file
            if image and image.filename != '':
                # Secure the filename and save the file to the upload folder
                image_filename = secure_filename(image.filename)
                upload_path = os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename)
                image.save(upload_path)
                new_product.image_url = f"media/{image_filename}"
            
            db.session.add(new_product)
            db.session.commit()
            flash("Product Created Successfully.")
            return redirect(url_for("product.show_products"))
        else:
            return form.errors

    # if the form is being asked for, render and return it
    return render_template("ProductForm.html", form=form, operation_name="Add")


@product.route("/update/<int:product_id>", methods=["GET", "POST"])
def update_product(product_id):
    product = Product.query.get(product_id)
    form = New_Product_Form(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        new_product = Product(
                name=form.name.data,
                price=form.price.data,
                description=form.description.data,
                product_category=form.product_category.data,
                # image_url=form.image_url.data,
                size=form.size.data,
                color=form.colour.data,
                quantity=form.quantity.data,
                manufacturer=form.manufacturer.data,
                country_of_origin=form.country_of_origin.data,
                rating=form.rating.data,
                discount=form.discount.data

            )
        image = form.image_url.data  # This is the uploaded file
        if image and image.filename != '':
            # Secure the filename and save the file to the upload folder
            image_filename = secure_filename(image.filename)
            upload_path = os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"], image_filename)
            image.save(upload_path)
            new_product.image_url = f"media/{image_filename}"
        
            db.session.add(new_product)
            db.session.commit()
        flash("Product Updated Successfully.")
        return redirect(url_for("product.show_products"))
    return render_template("ProductForm.html", form=form, operation_name="Update")


@product.route("/delete/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("product.show_products"))


@product.route("/upload/<image_filename>")
def get_image(image_filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], image_filename)
