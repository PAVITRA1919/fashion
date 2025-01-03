from flask import Blueprint, session, flash, redirect, url_for
# utils = Blueprint('utils', __name__)

def restrict_to_admin():
    if session.get('role') != 'admin':
        flash('Access denied! Admins only.', 'danger')
        return redirect(url_for('auth.login'))