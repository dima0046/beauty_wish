from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)# nullable - не может быть нуллом, сервер выдаст ошибку
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self): # self обращение к тому экземпляру класса, который сейчас активен
        return '<News {} {}>'.format(self.title, self.url) # Нужно, чтобы если захотели сделать print(),
                                                           # нам выводился результат в читабельном формате