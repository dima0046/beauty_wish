import requests

from webapp.db import db
from webapp.stores.models import Products, Stores
from sqlalchemy import update


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

def save_products(brand_full_string, brand_name, brand_product, url, image, price, category, store_id, subcategory, text):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    product_exists = Products.query.filter(Products.url == url).count()
    product_price = Products.query.filter(Products.url == url).first()
    store_exists = Stores.query.filter(Stores.id == store_id).count()
    # print(news_exists)
    
    if product_exists != 0:
        old_price =  int(product_price.price)
    price = int(price)
    
    # Сохранение нового продукта в БД
    if product_exists == 0:        
        new_product = Products(brand_full_string=brand_full_string, brand_name=brand_name, brand_product=brand_product,
                               url=url, image=image, price=price, text=text, category=category, store_id=store_id, subcategory=subcategory)
        db.session.add(new_product)
        db.session.commit()
    #Обновление цены на продукцию
    elif product_exists != 0 and product_price.price != price:
        product_price.price = price
        print(f'Цена продукта {brand_full_string} сменилась с {old_price} на {product_price.price}')
        db.session.commit()    
    else:
        print(f'Товар "{brand_full_string}" уже есть в базе')