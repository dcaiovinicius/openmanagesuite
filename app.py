from flask import Flask

from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from controllers.login import login_controller
        app.register_blueprint(login_controller)

    return app