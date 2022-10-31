from webapp.db import db
from sqlalchemy import ForeignKey

#from webapp.stores.views import index


class Stores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Subategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_full_string = db.Column(db.String, nullable=False)# nullable - не может быть нуллом, сервер выдаст ошибку
    brand_name = db.Column(db.String, nullable=False)
    brand_product = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=True)
    category = db.Column(db.String, nullable=False)
    subcategory = db.Column(db.String, nullable=False)
    #category = db.Column(db.Integer, db.ForeignKey('Category.id', ondelete='CASCADE'), index=True)
    #subcategory = db.Column(db.Integer, db.ForeignKey('Subcategory.id', ondelete='CASCADE'), index=True)
    store_id = db.Column(db.Integer, ForeignKey(Stores.id), index=True, nullable=False)

    def __repr__(self): # self обращение к тому экземпляру класса, который сейчас активен
        return f'<Product {self.id},  {self.brand_full_string}>' # Нужно, чтобы если захотели сделать print(),
                                                           # нам выводился результат в читабельном формате