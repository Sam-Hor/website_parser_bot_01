#in terminal source env/bin/activate :

from bs4 import BeautifulSoup
with open("index2.html") as file:
    src = file.read()

# нужно преобразовать код в дерево объектов python

soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# ищем
# .find() .find_all()

# ищем заголовки
# page_h1 = soup.find("h1")
# print(page_h1)

# ищем имя и выводим текст
# user_name = soup.find('div', class_='user__name')
# print(user_name.text.strip())

# перемещаем параметр текст сразу в поиск
# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

#передача словаря с параметром отбора с помощью парк-ключ значения
# user_name = soup.find("div", {class: "user__name", "id": "aaa"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# # вывод на печать списка
# for item in find_all_spans_in_user_info:
#     print(item.text)

# # работа со списком - взять 1 из элементов списка по индексу

# print(find_all_spans_in_user_info[0])
# # или применить метод
# print(find_all_spans_in_user_info[3].text)

# опуститься в код в глубь 
# social_links = soup.find(class_="social__networks").find('ul').find_all('a')
# print(social_links)

# 
# all_a = soup.find_all('a')
# print(all_a)

# проверка каждый ссылки с параметром атрибута href + cразу получаем методом текст
# for item in all_a:
#     item_text = item.text
#     item_url = item.get('href')
#     print(f"{item_text}: {item_url}")

# # методы с поиском по коду снизу вверх
# .find_parents() .find_parents()
# .find_parents()  забирает элемент не целиком а до первого родителя
# post_div = soup.find(class_='post__text').find_parent()
# print(post_div)

# .find_parents() забирает всё
# post_divs = soup.find(class_='post__text').find_parents()
# print(post_divs)

# .next_element .previous_element
# # .find_next аналогичный метод
# next_el = soup.find(class_='post__title').next_element.next_element.text
# # print(next_el)

# # next_el = soup.find(class_='post__title').find_next().text
# # print(next_el)

# # .find_next_sibling() .find_previous_sibling()
# # ищут и возвращают следующий/предыдущий элементы внутри тега
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

# #  возможны комбинации методов
# post_title = soup.find(class_="post__title").find_next_sibling().find_next().text
# print(post_title)


links = soup.find(class_="some__links").find_all("a")
print(links)

links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#
#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]
#
#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)

# расширение возможности за пределами bs4 через re.compile
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)

find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
print(find_all_clothes)