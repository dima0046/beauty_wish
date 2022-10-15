from getpass import getpass # Чтобы нельзя было подсмотреть пароль пользователя
import sys # Для работы sys exit

from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()

with app.app_context(): # обращаемся к приложению
    username = input('Введите имя пользователя: ') # обращение к командной строке

    if User.query.filter(User.username == username).count(): # фильтр на наличие пользователя
        print('Такой пользователь уже есть')
        sys.exit(0)

    email = input('Введите Email: ')
    if User.query.filter(User.email == email).count(): # фильтр на наличие пользователя
        print('Такой email уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        print('Пароли не совпадают')
        sys.exit(0)

    new_user = User(username=username, email=email, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))