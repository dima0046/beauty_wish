from webapp.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_full_string = db.Column(db.String, nullable=False)# nullable - не может быть нуллом, сервер выдаст ошибку
    brand_name = db.Column(db.String, nullable=False)
    brand_product = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    store = db.Column(db.String, nullable=False)

    def __repr__(self): # self обращение к тому экземпляру класса, который сейчас активен
        return '<Products {} {}>'.format(self.title, self.url) # Нужно, чтобы если захотели сделать print(),
                                                           # нам выводился результат в читабельном формате