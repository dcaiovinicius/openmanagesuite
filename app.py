from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from controllers.login import login_controller
        app.register_blueprint(login_controller)

        from controllers.products import products_controller
        app.register_blueprint(products_controller)

        from models import user, product
        db.create_all()
    return app

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))
