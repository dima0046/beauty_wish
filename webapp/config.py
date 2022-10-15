from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, '..', 'beautywish.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "nf9ewff9732jfjsduf"

REMEMBER_COOKIE_DURATION = timedelta(days=5) #запоминает на сколько надо сохранить авторизацию пользователя (flask login)