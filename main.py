from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from controllers.login import auth_bp
        app.register_blueprint(auth_bp)

    return app(venv)