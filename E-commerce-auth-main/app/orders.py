# app/routes.py
from flask import render_template, request, redirect, url_for,Blueprint
from app import app, db
from app.models import Order

orders=Blueprint('orders', __name__)
# Route to display the dashboard
@orders.route('/delivery_dashboard')
def index():
    deliveries = Order.query.all()  # Get all deliveries from the db
    return render_template('delivery_dashboard.html', deliveries=deliveries)

# Route to add new delivery
@orders.route('/add', methods=['POST'])
def add_delivery():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        status = request.form['status']

        new_delivery = Order(name=name, address=address, status=status)

        try:
            db.session.add(new_delivery)
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            return "There was an issue adding the delivery."

# Route to update delivery status
@orders.route('/update/<int:id>', methods=['GET', 'POST'])
def update_delivery(id):
    delivery = Order.query.get_or_404(id)

    if request.method == 'POST':
        delivery.status = request.form['status']
        try:
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            return "There was an issue updating the delivery."

    return render_template('update.html', delivery=delivery)
