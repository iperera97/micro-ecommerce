from marshmallow_sqlalchemy import SQLAlchemySchema
import marshmallow as ma
from models import Product


class ProductSchema(SQLAlchemySchema):
    price = ma.fields.Float()

    class Meta:
        model = Product
        fields = [
            "id", "sku", "name", "price",
            "discription", "image",
            "created", "updated"
        ]
        ordered = True
