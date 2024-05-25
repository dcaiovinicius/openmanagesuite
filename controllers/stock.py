from flask import Blueprint, render_template
import flask_login

stock_controller = Blueprint('stock_controller', __name__)

@stock_controller.route('/stock')
@flask_login.login_required
def stock_page():
    return "<h1>Stock</h1>"