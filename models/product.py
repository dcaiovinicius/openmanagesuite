from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(512))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, stock_quantity={self.stock_quantity}, active={self.active}, created_at={self.created_at}, updated_at={self.updated_at})>"
