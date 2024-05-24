from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_app():
    with app.app_context():
        from controllers.login import login_controller
        app.register_blueprint(login_controller)

    return app