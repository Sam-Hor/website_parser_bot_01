import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

data = []
for page in range(1, 13):
    print(page)
    url = f'https://journal.tinkoff.ru/flows/sravnyator/best/page/{page}/'
    r = requests.get(url)
    sleep(3)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    all_titles = soup.findAll('div', class_='header--T3Cfh')
    for i in all_titles:
        date = i.find('div', class_='nowrap--wLyr4').find('time').text
        print(date)
        title = i.find('a', class_='link--r6yOY').text
        author = i.find('div', class_='name--tpxhM').text
        print(title, '//', author)
        link = i.find('a', class_='link--r6yOY').get('href')
        print('https://journal.tinkoff.ru'+link)
                  

        data.append([date, title, author, link])
header = ['date', 'title', 'author', 'link']
df = pd.DataFrame(data, columns=header) 
df.to_csv('/Users/Sam/Python_razr/website_parser_bot_01/parser.csv', sep=';', encoding='utf8')       

          
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
