from datetime import datetime

from bs4 import BeautifulSoup # Для упрощённой работы с HTML

from webapp.stores.parsers.utils import get_html, save_products

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
            brand_product = brand_full_string_list[-1].lstrip()

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

            # категория
            category = "Макияж"

            # подкатегория
            subcategory = "Глаза"

            #Название магазина
            store_id = 1

            #Описание продукта
            html1 = get_html(url)
            text1=""
            if html1:
                soup1 = BeautifulSoup(html1, "html.parser")
                text1 = soup1.find('div', class_='__text').text

            save_products(brand_full_string, brand_name, brand_product, url, image, price, category, store_id, subcategory, text1)

