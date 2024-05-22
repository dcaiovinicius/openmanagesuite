from flask import Blueprint, jsonify, render_template

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/')
def login():
    return render_template('login.html')