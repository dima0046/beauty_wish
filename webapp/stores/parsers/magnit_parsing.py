from datetime import datetime

from bs4 import BeautifulSoup # Для упрощённой работы с HTML

from webapp.stores.parsers.utils import get_html, save_products

def get_magnit_make():
    html = get_html("https://magnitcosmetic.ru/catalog/kosmetika/makiyazh_glaz/teni_i_bazy_dlya_vek/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_brands_list = soup.find('div', class_='catalog__list')  # Нашли на странице нужный класс
        #print(brand_full_string)
        all_brands_list = all_brands_list.findAll('div', class_='catalog__item')
        for item in all_brands_list:
            # ищем название бренда и продукта
            brand_full_string = item.find('a', class_='product__title').text
            brand_full_string_list = str(brand_full_string).split("`")
            brand_name = brand_full_string_list
            brand_product = brand_full_string_list

            # ссылка магазина на продукт
            url = item.find('a', class_='product__link')['href']
            url = "https://magnitcosmetic.ru" + url

            # картинка
            image = item.find('a', class_='product__link')
            image = item.find('img')['src']
            image = "https://magnitcosmetic.ru" + image

            # цена
            price = item.find('div', class_='item-price_value js-item_price-value').text            

            # категория
            category = "Макияж"

            # подкатегория
            subcategory = "Глаза"

            #Название магазина
            store_id = 3

            #Описание продукта
            html1 = get_html(url)
            text1=""
            if html1:
                soup1 = BeautifulSoup(html1, "html.parser")
                text1 = soup1.find('div', class_='action-card__text').text

            save_products(brand_full_string, brand_name, brand_product, url, image, price, category, store_id, subcategory, text1)

