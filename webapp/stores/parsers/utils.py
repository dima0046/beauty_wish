import requests

from webapp.db import db
from webapp.stores.models import Products, Stores


def get_html(url): #принимает url
    headers = {
        'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'   #Заголовок, чтобы было видно, что заходит человек
    }
    try:
        result = requests.get(url) # Базовый запрос. Берем данные из этого url
        result.raise_for_status() # Перехват ошибок 4хх и 5хх
        return result.text # Если всё хорошо
    except(requests.RequestException, ValueError):  # RequestException - если сетевая проблема,
                                                    # ValueError - если на стороне сервера возникла проблема
        print("Сетевая ошибка")
        return False

def save_products(brand_full_string, brand_name, brand_product, url, image, price, category, store_id, subcategory):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    product_exists = Products.query.filter(Products.brand_full_string == brand_full_string).count()
    store_exists = Stores.query.filter(Stores.id == store_id).count()
    # print(news_exists)
    if product_exists == 0:
        # запись данных в БД
        new_product = Products(brand_full_string=brand_full_string, brand_name=brand_name, brand_product=brand_product,
                               url=url, image=image, price=price, category=category, store_id=store_id, subcategory=subcategory)
        db.session.add(new_product)
        db.session.commit()
    else:
        print(f'Товар "{brand_full_string}" уже есть в базе')