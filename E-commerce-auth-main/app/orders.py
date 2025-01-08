from flask import render_template, request, jsonify, Blueprint,session,flash,redirect,url_for
from . import db
from .models import Order

orders = Blueprint('orders', __name__)

@orders.route('/delivery_dashboard')
def delivery_person():
    if session.get('role') != 'delivery_person':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('auth.login'))
    all_orders = db.session.query(Order).all()
    return render_template("delivery_dashboard.html", order=all_orders)
@orders.route('/orders', methods=['GET'])
def delivery_dashboard():
    orders = Order.query.all()  # Assuming you want all orders
    # return render_template('delivery_dashboard.html', orders=order_data)
    orders = db.session.query(Order).all()
    order_data = [
        {
            'id': order.id,
            'order_amount': order.order_amount,
            'order_date': order.order_date.strftime('%Y-%m-%d'),
            'user_id': order.user_id,
            'product_id': order.product_id,
            'status': order.status,
            'payment_method': order.payment_method
        }
        for order in orders
    ]
    return render_template('delivery_dashboard.html', orders=order_data)

@orders.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    order_id = data['id']
    new_status = data['status']
    # print(new_status)
    try:
        order = Order.query.get(order_id)
        if order:
            order.status = new_status
            db.session.commit()
            orders = Order.query.all()
            order_data = [
                {
                    'id': order.id,
                    'order_amount': order.order_amount,
                    'order_date': order.order_date.strftime('%Y-%m-%d'),
                    'user_id': order.user_id,
                    'product_id': order.product_id,
                    'status': order.status,
                    'payment_method': order.payment_method
                }
                for order in orders
            ]
            return jsonify({'message': 'Status updated successfully', 'order_id': order_id, 'new_status': new_status, 'html': render_template('order_status_update.html', orders=order_data)}), 200
        else:
            return jsonify({'error': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
                                                