import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

data = []

for page in range(1, 14):
    print(page)
    url = f'https://journal.tinkoff.ru/flows/sravnyator/best/page/{page}/'
    r = requests.get(url)
    sleep(3)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    all_titles = soup.findAll('div', class_='item--HhAuM')
    for i in all_titles:
        header_div = i.find('div', class_='header--T3Cfh')
        if header_div is not None:
            date = header_div.find(
                'div', class_='nowrap--wLyr4').find('time').text
       
            title = i.find('a', class_='link--r6yOY').text
            author = i.find('div', class_='name--tpxhM').text
        
            link = i.find('a', class_='link--r6yOY').get('href')
            try:
                likes = i.find('div', class_='footer--Crxl1').find('span', class_='counter--JYT17').text
            except:
                likes = "-"
            comments = i.find('div', class_='footer--Crxl1').find('span', class_='content--po_Ru').text
            notes = i.find('div', class_='footer--Crxl1').find('div', class_='meta--owULW').find('button', class_='favorites--ugnex').text
       
        print(date, title, '//', author)
        print('likes:', likes, 'comments:', comments, 'notes:', notes)
        print()

        data.append([date, title, author, link, likes, comments, notes])

header = ['date', 'title', 'author', 'link', 'likes', 'comments', 'notes']
df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/Sam/Python_razr/website_parser_bot_01/parser01.csv', sep=';', encoding='utf8')
