from app import create_app, db
from models.user import User
from models.product import Product

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="admin", email="admin@gmail.com")
    user.set_password("password")

    db.session.add(user)
    db.session.commit()

    products = [
        {
            "name": "iPhone 13",
            "description": "Latest iPhone model with advanced features.",
            "price": 1099.99,
            "stock_quantity": 100,
            "active": True
        },
        {
            "name": "MacBook Pro",
            "description": "Powerful laptop for professionals.",
            "price": 1999.99,
            "stock_quantity": 50,
            "active": True
        },
        {
            "name": "Samsung Galaxy S22",
            "description": "Android smartphone with high-end specs.",
            "price": 999.99,
            "stock_quantity": 75,
            "active": True
        },
        {
            "name": "Dell XPS 15",
            "description": "Premium Windows laptop with stunning display.",
            "price": 1799.99,
            "stock_quantity": 30,
            "active": True
        },
        {
            "name": "iPad Air",
            "description": "Lightweight tablet with powerful performance.",
            "price": 599.99,
            "stock_quantity": 80,
            "active": True
        },
        {
            "name": "HP Spectre x360",
            "description": "Convertible laptop with sleek design.",
            "price": 1299.99,
            "stock_quantity": 25,
            "active": True
        },
        {
            "name": "Google Pixel 6",
            "description": "Flagship smartphone with great camera capabilities.",
            "price": 899.99,
            "stock_quantity": 60,
            "active": True
        },
        {
            "name": "Lenovo ThinkPad X1 Carbon",
            "description": "Business laptop with durable construction.",
            "price": 1599.99,
            "stock_quantity": 40,
            "active": True
        },
        {
            "name": "Sony PlayStation 5",
            "description": "Next-gen gaming console with cutting-edge technology.",
            "price": 499.99,
            "stock_quantity": 20,
            "active": True
        },
        {
            "name": "Microsoft Surface Pro 8",
            "description": "Versatile 2-in-1 device for work and creativity.",
            "price": 1299.99,
            "stock_quantity": 35,
            "active": True
        }
    ]

    for product_data in products:
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            stock_quantity=product_data["stock_quantity"],
            active=product_data["active"]
        )

        db.session.add(product)

    db.session.commit()
