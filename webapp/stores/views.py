from flask import Blueprint, render_template
from webapp.stores.models import Products, Stores
from webapp.db import db

blueprint = Blueprint('products', __name__)

@blueprint.route('/')  # декоратор
def index():
    page_title = "Beauty Wish"
    # weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
    # get_podrujka_make()


    #product_list = Products.query.all()
    return render_template('products/index.html', page_title=page_title, product_list=product_list)