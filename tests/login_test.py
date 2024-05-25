from models.user import User
from app import db

def test_login_page(client):
    response = client.get("/")
    assert b"<h1>Entre com seu log-in</h1>" in response.data

def test_invalid_user(client):
    response = client.post('/login', data={
        'username': 'joe',
        'password': 'password'
    }, follow_redirects=True)

    # bytes can only contain ASCII literal characters
    assert b'<p>Invalid username or password</p>' in response.data

def test_valid_user(client):
    user = User(username="admin", email="admin@gmail.com")
    user.set_password("password")

    db.session.add(user)
    db.session.commit()

    response = client.post('/login', data={
        'username': 'admin',
        'password': 'password'
    }, follow_redirects=True)

    assert b'Stock' in response.data
