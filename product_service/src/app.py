from flask.views import MethodView
from flask_smorest import Blueprint

from config import app, db, api
from models import Product
from schemas import ProductSchema

blp = Blueprint(
    'products', "products", url_prefix='/api/products',
    description='Product management'
)


@blp.route("/")
class ProductsView(MethodView):

    @blp.response(ProductSchema(many=True))
    def get(self, *args, **kwargs):
        return Product.query.all()


@blp.route("/<product_id>")
class ProductView(MethodView):

    @blp.response(ProductSchema)
    def get(self, product_id):
        return Product.query.get_or_404(product_id)


api.register_blueprint(blp)
