from ast import Store
from itertools import product
from flask import abort, Blueprint, current_app, render_template
from webapp.stores.models import Products, Stores
from webapp.db import db

blueprint = Blueprint('products', __name__)

@blueprint.route('/')  # декоратор
def index():
    page_title = "Beauty Wish"
    # weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
    # get_podrujka_make()


    product_list = Products.query.all()
    #product_list1 = Products.query.
    return render_template('products/index.html', page_title=page_title, product_list=product_list)

@blueprint.route('/product/<int:product_id>')
def single_item(product_id):
    my_product = Products.query.filter(Products.id == product_id).first()
    store_name = Stores.query.filter(Stores.id == my_product.store_id).first()
    if not my_product:
        abort(404)

    return render_template('products/single_product.html', page_title=my_product.brand_full_string, store=store_name.name, price=my_product.price)
