import requests
from bs4 import BeautifulSoup # Для упрощённой работы с HTML

def get_html(url): #принимает url
    try:
        result = requests.get(url) # Базовый запрос. Берем данные из этого url
        result.raise_for_status() # Перехват ошибок 4хх и 5хх
        return result.text # Если всё хорошо
    except(requests.RequestException, ValueError):  # RequestException - если сетевая проблема,
                                                    # ValueError - если на стороне сервера возникла проблема
        print("Сетевая ошибка")
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find('ul', class_='list-recent-posts menu') # Нашли на странице нужный класс
        all_news = all_news.findAll('li') # Нашли внутри результатов предыдущиего поиска определённый список
        result_news = []
        for news in all_news:
            title = news.find('a').text # Найти содержимое атрибута <a></a>  внутри каждого элемента списка
            url = news.find('a')['href'] # К атрибутам обращаться как к словарю, а к содержимому через точку
            published = news.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                "published": published
            })
        return result_news
    return False
