from flask import Blueprint, render_template, request
import flask_login

from models.product import Product

products_controller = Blueprint('products_controller', __name__)

@products_controller.route('/products')
@flask_login.login_required
def index():
    search_term = request.args.get('query', '')
    if search_term:
        products = Product.query.filter(Product.name.ilike(f'%{search_term}%')).all()
    else:
        products = Product.query.all()

    return render_template('products/index.html', products=products)
