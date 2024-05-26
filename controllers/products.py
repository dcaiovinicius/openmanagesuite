from flask import Blueprint, render_template
import flask_login

products_controller = Blueprint('products_controller', __name__)

@products_controller.route('/products')
@flask_login.login_required
def index():
    return render_template('products/index.html')
