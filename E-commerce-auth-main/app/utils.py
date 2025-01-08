from flask import Blueprint, session, flash, redirect, url_for
# utils = Blueprint('utils', __name__)

# def restrict_to_admin():
    # if session.get('role') != 'admin':
    #     flash('Access denied! Admins only.', 'danger')
    #     return redirect(url_for('auth.login'))
    
from flask import session, redirect, url_for,flash
from functools import wraps

def restrict_to_admin():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') != 'admin':
                # Redirect to login or unauthorized access page
                flash('Access denied! Admins only.', 'danger')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def restrict_to_deliveryPerson():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') != 'delivery_person':
                # Redirect to login or unauthorized access page
                flash('Access denied! DeliveryPerson only.', 'danger')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
