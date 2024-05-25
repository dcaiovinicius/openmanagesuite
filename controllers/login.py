from flask import Blueprint, render_template, request, redirect
from models.user import User
import flask_login

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/')
def new():
    return  """
    <h1>Entre com seu log-in</h1>
    <form method="POST" action="/login">
      username: <input name="username"><br>
      Password: <input name="password" type=password><br>
      <button>Log In</button>
    </form>
    """


@login_controller.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password_hash(password):
            return "<p>Invalid username or password</p>"
        else:
            flask_login.login_user(user)
            return redirect('stock')