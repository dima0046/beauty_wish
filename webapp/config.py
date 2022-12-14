from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, '..', 'beautywish.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False 

SECRET_KEY = "nf9ewff9732jfjsduf"

REMEMBER_COOKIE_DURATION = timedelta(days=5) #запоминает на сколько надо сохранить авторизацию пользователя (flask login)

STORE_LIST = ['Подружка', 'Золотое яблоко', 'Магнит Косметик']
CATEGORY_LIST = ['Макияж', 'Уход', 'Волосы', 'Парфюмерия']
SUBCATEGORY_LIST = ['Лицо', 'Глаза', 'Губы', 'Брови','Ногти', 'Кисти и спонжи']