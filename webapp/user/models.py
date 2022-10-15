from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db

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

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self): # Чтобы выводить на экран читабельный вид юзера
        return '<User {}>'.format(self.username)