from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

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

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(300), unique=True)
    role = db.Column(db.String(10), index=True)

    def set_password(self, password): #зашифровывает строку password. зависит от secret_key
        self.password = generate_password_hash(password)

    def check_password(self, password):# возвращает значение функции generate_password_hash
        return check_password_hash(self.password, password)

    def __repr__(self): # Чтобы выводить на экран читабельный вид юзера
        return '<User {}>'.format(self.username)