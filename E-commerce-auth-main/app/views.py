from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .admin import admin_dashboard
from .orders import delivery_dashboard,update_status
from .utils import restrict_to_deliveryPerson,restrict_to_admin
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

# @main.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', username=current_user.username)

# @main.route('/profile')
# @login_required
# def profile():
#     return f"Welcome, {current_user.username}. Your role is {current_user.role}."

@main.route('/customer_dashboard')
def customer_dashboard():
    return render_template('customer_dashboard.html')  # Create this template

@main.route('/delivery_dashboard')
def delivery():
    return delivery_dashboard()
    # return render_template('delivery_dashboard.html')  # Create this template
@main.route('/update_status', methods=['POST'])
@restrict_to_deliveryPerson()
def order():
    return update_status()
@main.route('/default_dashboard')
def default_dashboard():
    return render_template('default_dashboard.html')  # Create this template

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Fallback or general dashboard

@main.route('/forms')
@restrict_to_admin()
def forms():
    return render_template('ProductForm.html')

@main.route('/product')
@restrict_to_admin()
def product():
    return render_template('all_products.html')
