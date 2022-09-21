import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_python_news(html):
    soup = BeautifulSoup(html, "html.parser")
    all_news = soup.find('ul', class_='list-recent-posts menu')
    all_news = all_news.findAll('li')
    result_news = []
    print(all_news)

if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        get_python_news(html)
        #Результат работы скрипта файла
        #with open("python.org.html", "w", encoding="utf8") as f:
        #    f.write(html)