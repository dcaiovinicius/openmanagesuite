from app import create_app, db
from models.user import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="admin", email="admin@gmail.com")
    user.set_password("password")

    db.session.add(user)
    db.session.commit()
