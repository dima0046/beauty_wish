from webapp.db import db
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

#from webapp.stores.views import index


class Stores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Subategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
    db.Integer,
    db.ForeignKey('category.id', ondelete='CASCADE'), # Поведение при удалении. Если удаляется новость,
                                                        # то все комментарии удаляютс автоматически
    index=True # Точная комманда, что индекс надо создавать. перестраховка
    )
    name = db.Column(db.String, nullable=False)

    products = relationship('Category', backref='Subategory')


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_full_string = db.Column(db.String, nullable=False)# nullable - не может быть нуллом, сервер выдаст ошибку
    brand_name = db.Column(db.String, nullable=False)
    brand_product = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategory = db.Column(db.String, nullable=False)
    #category = db.Column(db.Integer, db.ForeignKey('Category.id', ondelete='CASCADE'), index=True)
    #subcategory = db.Column(db.Integer, db.ForeignKey('Subcategory.id', ondelete='CASCADE'), index=True)
    store_id = db.Column(db.Integer, ForeignKey(Stores.id), index=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    products = relationship('Category', backref='products')


    def comments_count(self):
        return Comment.query.filter(Comment.product_id == self.id).count()

    def __repr__(self): # self обращение к тому экземпляру класса, который сейчас активен
        return f'<Product {self.id},  {self.brand_full_string}>' # Нужно, чтобы если захотели сделать print(),
                                                           # нам выводился результат в читабельном формате

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('products.id', ondelete='CASCADE'), # Поведение при удалении. Если удаляется новость,
                                                          # то все комментарии удаляютс автоматически
        index=True # Точная комманда, что индекс надо создавать. перестраховка
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    products = relationship('Products', backref='comments')
    user = relationship('User', backref='comments')
    def __repr__(self):
        return '<Comment {}>'.format(self.id)