import requests
from bs4 import BeautifulSoup  # Для упрощённой работы с HTML

from webapp.db import db
from webapp import create_app
from webapp.stores.models import Stores
from webapp.config import STORE_LIST


def save_stores(store_name):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    news_exists = Stores.query.filter(Stores.name == store_name).count()
    # print(news_exists)
    if not news_exists:
        # запись данных в БД
        new_store = Stores(name=store_name)
        db.session.add(new_store)
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():  # функция, чтобы обращаться к бд
        for store_name in STORE_LIST:
            save_stores(store_name)
