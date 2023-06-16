import requests
from bs4 import BeautifulSoup

for page in range(1, 12):
    url = f'https://journal.tinkoff.ru/flows/sravnyator/best/page/{page}/'

    r = requests.get(url)
    r.encoding = 'utf-8'
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
# href обязательный атрибут для ссылок

# titles = soup.find('div', class_='header--T3Cfh')
# print(titles.text)
# print()

# ======задача вывести и лайки и заметки после каждой записи


# 1 успех
    all_titles = soup.findAll('div', class_='header--T3Cfh')
    for i in all_titles:
        date = i.find('div', class_='nowrap--wLyr4').find('time').text
        print(date)
        title = i.find('a', class_='link--r6yOY').text
        author = i.find('div', class_='name--tpxhM').text
        print(title, '//', author)
        link = i.find('a', class_='link--r6yOY').get('href')
        print('https://journal.tinkoff.ru'+link)

# data.append([date, title, author, link])

# 2
# all_titles = soup.findAll('div', class_='item--HhAuM')
# for i in all_titles:
#     date = i.find('div', class_='header--T3Cfh').find('div', class_='nowrap--wLyr4').find('time')
#     print(date.text)
#     title = i.find('a', class_='link--r6yOY')
#     author = i.find('div', class_='name--tpxhM')
#     print(title.text, '//', author.text)
#     link = i.find('a', class_='link--r6yOY').get('href')
#     print('https://journal.tinkoff.ru'+link)

# footer--Crxl1
    # likes = i.find('span', class_='counter--JYT17')
    # comments = i.find('span', class_='content--po_Ru')
    # notes = i.find('div', class_='meta--owULW').get('span')
    # # .find('button', class_='favorites--ugnex')
    # print('likes:', likes, 'comments:', comments, 'notes:', notes)
    # print()
