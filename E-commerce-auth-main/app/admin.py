from flask import Blueprint, render_template, flash, redirect, url_for, session
from .models import User
from .import db, bcrypt
from datetime import datetime

admin = Blueprint('admin', __name__)

def create_admin_user():
    admin = User.query.filter_by(email='admin@gmail.com').first()
    if not admin:
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        new_admin = User(
            username='admin',
            email='admin@gmail.com',
            password=hashed_password,
            role='admin',
            contact='1234567890',
            location='Admin Location',
            dob=datetime(1990, 1, 1).date(),
            gender='male'
        )
        db.session.add(new_admin)
        db.session.commit()

@admin.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('auth.login'))
    delivery_requests = User.query.filter_by(role='delivery_person', status='pending').all()
    return render_template('all_products.html',delivery_requests=delivery_requests ,username=session.get('username'))


# @admin.route('/product')
# # @admin_dashboard
# def product_page():
#     if session.get('role') != 'admin':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))
#     return render_template('ProductForm.html', username=session.get('username'))


# @admin.route('/delivery_dashboard')
# # @admin_dashboard
# def delivery_dashboard():
#     if session.get('role') != 'customer':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))
#     return render_template('delivery_dashboard.html', username=session.get('username'))









# from flask import Blueprint, render_template, flash, redirect, url_for, session
# from .models import User
# from . import db, bcrypt
# from datetime import datetime
# from .utils import restrict_to_admin

# admin = Blueprint('admin', __name__)

# def create_admin_user():
#     admin = User.query.filter_by(email='admin@gmail.com').first()
#     if not admin:
#         hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
#         new_admin = User(
#             username='admin',
#             email='admin@gmail.com',
#             password=hashed_password,
#             role='admin',
#             contact='1234567890',
#             location='Admin Location',
#             dob=datetime(1990, 1, 1).date(),
#             gender='male'
#         )
#         db.session.add(new_admin)
#         db.session.commit()



# @admin.route('/admin_dashboard')
# # @restrict_to_admin 
# def admin_dashboard():
#     if session.get('role') != 'admin':
#         flash('Unauthorized access!', 'danger')
#         return redirect(url_for('auth.login'))
#     delivery_requests = User.query.filter_by(role='delivery_person', status='pending').all()
#     return render_template('all_products.html',delivery_requests=delivery_requests ,username=session.get('username'))



# @admin.route('/product')
# # @restrict_to_admin 
# def product_page():
#     if session.get('role') != 'admin':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))
#     return render_template('ProductForm.html', username=session.get('username'))



# @admin.route('/delivery_dashboard') 
# # @restrict_to_admin 
# def delivery_dashboard():
#     if session.get('role') != 'customer':
#         flash('Access denied! Admins only.', 'danger')
#         return redirect(url_for('auth.login'))
#     return render_template('delivery_dashboard.html', username=session.get('username'))