from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_mail import Mail
from dotenv import load_dotenv
# from .models import db
# from .product import product_blueprint
import os
# from .models import User,Order,Cart,Wishlist,Product
# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()  # Will be initialized after app creation
mail=Mail()

load_dotenv()
print(f"MAIL_USERNAME: {os.getenv('MAIL_USERNAME')}")

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Application configuration
    secret_key = 'mysecretkey'
    print(f"SECRET_KEY: {secret_key}")  # Debugging output
    app.config['SECRET_KEY'] = secret_key
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False  # Disable SSL when using TLS
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Add your email
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Add your email password or app-specific password
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    app.config['UPLOAD_FOLDER'] = 'media'
    os.makedirs(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']), exist_ok=True)
    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    # Login settings
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Please log in to access this page."

    # Define the user_loader function
    from .models import User, Order, Cart, Wishlist, Product
    # Creates the db tables # Import after db.init_app(app) to avoid circular imports
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Fetch the user by ID

    # Register blueprints
    from .views import main
    from .auth import auth
    from .password import password
    from .admin import admin
    from .request import request
    from .product import product
    from .forms import forms
    from .orders import orders
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(admin)
    app.register_blueprint(forms,url_prefix="/forms")
    app.register_blueprint(product,url_prefix='/product')
    # app.register_blueprint(admin, url_prefix="/admin")
    # app.register_blueprint(product_blueprint)
    # db creation and admin user setup
    app.register_blueprint(password,url_prefix="/password")
    app.register_blueprint(request,url_prefix="/request")
    app.register_blueprint(orders,url_prefix="/orders")
    with app.app_context():
        db.create_all()  # Creates db tables
        from .admin import create_admin_user  # Assuming this function exists in admin.py
        create_admin_user()
    
    #print(app.url_map)

    return app




