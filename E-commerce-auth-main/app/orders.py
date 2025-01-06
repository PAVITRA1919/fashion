# # app/routes.py
# # deliverydashboard.py

# # from flask import render_template, request, jsonify, Blueprint
# # from . import db
# # from .models import Order

# # orders = Blueprint('orders', __name__)

# # # Route to display the dashboard
# # @orders.route('/deliverydashboard', methods=['GET'])
# # def delivery_dashboard():
# #     # orders = Order.query.all()
# #     orders = db.session.query(Order).all()
# #     order_data = [
# #         {
# #             'id': order.id,
# #             'order_amount': order.order_amount,
# #             'order_date': order.order_date.strftime('%Y-%m-%d'),
# #             'user_id': order.user_id,
# #             'product_id': order.product_id,
# #             'status': order.status,
# #             'payment_method': order.payment_method
# #         }
# #         for order in orders
# #     ]
# #     return render_template('delivery_dashboard.html', orders=order_data)

# # # Route to update delivery status
# # @orders.route('/update_status', methods=['POST'])
# # def update_status():
# #     data = request.json
# #     order_id = data['id']
# #     new_status = data['status']

# #     order = Order.query.filter_by(id=order_id).first()
# #     if order:
# #         order.status = new_status
# #         db.session.commit()
# #         return jsonify({'message': 'Status updated successfully', 'order_id': order_id, 'new_status': new_status}), 200
# #     else:
# #         return jsonify({'error': 'Order not found'}), 404


from flask import render_template, request, jsonify, Blueprint
from . import db
from .models import Order

orders = Blueprint('orders', __name__,url_prefix="/delivery_dashboard")

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
    # order_data = []
    # for order in orders:
    # # Assuming you want to include user and product details in the order data
    #     user = order.user
    #     product = order.product   

    #     order_data.append({
    #         'order_id': order.id,
    #         'order_amount': order.order_amount,
    #         'order_date': order.order_date.strftime('%Y-%m-%d'),  # Format date for better readability
    #         'user': {
    #             'user_id': user.id,
    #             'username': user.username,
    #             'email': user.email,
    #             # Include other user details as needed
    #         },
    #         'product': {
    #             'product_id': product.id,
    #             'name': product.name,
    #             'price': product.price,
    #             'description': product.description,
    #             # Include other product details as needed
    #         },
    #         'status': order.status,
    #         'payment_method': order.payment_method,
    #     })
    # print(order_data)
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
                                                