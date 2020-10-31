from sqlalchemy.sql import func

from config import db


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(12), unique=True)
    name = db.Column(db.String(64))
    discription = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2))
    image = db.Column(db.Text, nullable=True)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __str__(self):
        return f"{self.id}-{self.name}"
