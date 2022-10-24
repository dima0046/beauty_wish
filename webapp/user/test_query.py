from webapp.stores.models import Products, Stores
from webapp.db import db

product_list = db.query(Products, Stores).join(Products.brand_full_string, Products.store_id == Stores.id).all()
print(product_list)