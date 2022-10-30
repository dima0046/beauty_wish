import requests
from bs4 import BeautifulSoup  # Для упрощённой работы с HTML

from webapp.db import db
from webapp import create_app
from webapp.stores.models import Subategory, Category, Stores
from webapp.config import STORE_LIST, CATEGORY_LIST, SUBCATEGORY_LIST


def save_stores(store_name):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    store_exists = Stores.query.filter(Stores.name == store_name).count()
    # print(news_exists)
    if not store_exists:
        # запись данных в БД
        new_store = Stores(name=store_name)
        db.session.add(new_store)
        db.session.commit()

def save_category(category_name):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    category_exists = Category.query.filter(Category.name == store_name).count()
    # print(news_exists)
    if not category_exists:
        # запись данных в БД
        new_category = Category(name=category_name)
        db.session.add(new_category)
        db.session.commit()

def save_subcategory(subcategory_name):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    subcategory_exists = Subategory.query.filter(Subategory.name == subcategory_name).count()
    # print(news_exists)
    if not subcategory_exists:
        # запись данных в БД
        new_subcategory = Subategory(name=subcategory_name)
        db.session.add(new_subcategory)
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():  # функция, чтобы обращаться к бд
        for store_name in STORE_LIST:
            save_stores(store_name)

        for category_name in CATEGORY_LIST:
            save_category(category_name)

        for subcategory_name in SUBCATEGORY_LIST:
            save_subcategory(subcategory_name)
