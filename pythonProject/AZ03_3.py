# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

# Настройка Selenium
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Фоновый режим (без открытия браузера)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

# URL для парсинга
base_url = "https://www.divan.ru/nizhny-novgorod/category/divany-i-kresla/page-"

# Список для хранения данных
data = []

# Парсим 10 страниц
for page in range(1, 5):
    url = base_url + str(page)
    driver.get(url)
# driver.get(base_url)
    time.sleep(3)  # Ждем загрузки страницы

    # Ищем элементы с ценами
    prices = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH')  # Цены

    for price in prices:
        data.append([price.text])

# Закрываем браузер
driver.quit()

# Сохраняем в CSV
columns = ["price"]
df = pd.DataFrame(data, columns=columns)
df.to_csv("prices.csv", index=False, encoding='utf-8')

print("Данные успешно сохранены в prices.csv")
