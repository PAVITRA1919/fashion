from app import create_app, db
from app.models import User, Product, Cart, Wishlist, Order
# Create the app instance using the factory function
app = create_app()
# Create the db and tables
# @app.before_first_request
# def create_tables():
#     db.create_all()
if __name__ == '__main__':
    app.run(debug=True)  # Runs in debug mode for easier development
