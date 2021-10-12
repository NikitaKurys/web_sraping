import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
KEYWORDS_1 = {'IT-стандарты', 'C++', 'web', 'python'}
res = requests.get("https://habr.com/ru/all/")


soup = BeautifulSoup(res.text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.find('span').text for hub in hubs)
    href = article.find(class_="tm-article-snippet__title-link").attrs['href']
    if KEYWORDS_1 & hubs:
        print(f"Дата: {article.find('time').text}")
        print(f"Заголовок: {article.find('h2').text}")
        print(f"Ссылка: {'https://habr.com' + href}", end='\n\n')

