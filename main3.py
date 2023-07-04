from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib.request
import pandas as pd

# Конфигурация пути до директории с изображениями
images_folder = '/Users/Sam/Python_razr/website_parser_bot_01/images/ramen'
# Убедитесь, что путь до папки существует или создайте его

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

data = []

# Инициализация webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.samyangfoods.com/eng/brand/list.do'
driver.get(url)

# Инициализируем объект WebDriverWait с ожиданием в 20 секунд
wait = WebDriverWait(driver, 120)

# Ожидаем, пока не появится элемент, который гарантированно появляется после загрузки всех продуктов
# В этом примере используется сам список продуктов, который появляется на странице после загрузки продуктов
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-list"]//img')))

# Затем находим все элементы продукта
products = driver.find_elements(By.XPATH, '//div[@class="product-list"]//li')

for product in products:
    title = product.find_element(By.XPATH, './div[2]').text
    image_url = product.find_element(By.XPATH, './div[1]/a/img').get_attribute('src')

    # Скачиваем и сохраняем изображение
    image_name = os.path.join(images_folder, image_url.split('/')[-1])
    urllib.request.urlretrieve(image_url, image_name)

    # Добавляем информацию о продукте в список данных
    data.append([title, image_url, image_name])

# Закрываем браузер
driver.quit()

# Сохраняем данные в CSV
df = pd.DataFrame(data, columns=['title', 'link', 'images'])
df.to_csv('/Users/Sam/Python_razr/website_parser_bot_01/ramen01.csv', sep=';', encoding='utf8')
