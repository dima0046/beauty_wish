from datetime import datetime

import requests
from bs4 import BeautifulSoup # Для упрощённой работы с HTML

from webapp.db import db
from webapp.stores.models import Products

def get_html(url): #принимает url
    try:
        result = requests.get(url) # Базовый запрос. Берем данные из этого url
        result.raise_for_status() # Перехват ошибок 4хх и 5хх
        return result.text # Если всё хорошо
    except(requests.RequestException, ValueError):  # RequestException - если сетевая проблема,
                                                    # ValueError - если на стороне сервера возникла проблема
        print("Сетевая ошибка")
        return False


def get_podrujka_make():
    html = get_html("https://www.podrygka.ru/catalog/makiyazh/glaza/teni/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_brands_list = soup.find('div', class_='products-list')  # Нашли на странице нужный класс
        all_brands_list = all_brands_list.findAll('div', class_='item-product-card')
        for item in all_brands_list:
            # ищем название бренда и продукта
            brand_full_string = item.find('a', class_='products-list-item__title').text
            brand_full_string_list = str(brand_full_string).split("`")
            brand_name = brand_full_string_list[1]
            brand_product = brand_full_string_list[2].lstrip()

            # ссылка магазина на продукт
            url = item.find('a', class_='products-list-item__title')['href']
            url = "https://www.podrygka.ru" + url

            # картинка
            image = item.find('a', class_='products-list-item__header')
            image = item.find('img')['src']
            image = "https://www.podrygka.ru" + image

            # цена
            price = item.find('div', class_='value one_price value--current')
            price = item.find('span').text

            #Название магазина
            store = "podrujka"

            #print(brand_full_string, brand_name, brand_product, url, image, price, store)

            # print(brand_name, brand_product)
            save_products(brand_full_string, brand_name, brand_product, url, image, price, store)


def save_products(brand_full_string, brand_name, brand_product, url, image, price, store):
    # проверка на повтор, чтобы не ругалась программа при повторной выгрузке
    news_exists = Products.query.filter(Products.url == url).count()
    # print(news_exists)
    if not news_exists:
        # запись данных в БД
        new_product = Products(brand_full_string=brand_full_string, brand_name=brand_name, brand_product=brand_product,
                               url=url, image=image, price=price, store=store)
        db.session.add(new_product)
        db.session.commit()
