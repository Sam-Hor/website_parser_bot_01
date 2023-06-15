import requests
from bs4 import BeautifulSoup


url = 'https://journal.tinkoff.ru/pro/'
r = requests.get(url)
r.encoding = 'utf-8'
# print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
# href обязательный атрибут для ссылок
a = soup.find('div', class_='card--P0w4a').find('div',
                                                class_='title--xDW1O').find('span')
print(a.string)
