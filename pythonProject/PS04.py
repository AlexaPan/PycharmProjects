# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# 4. Позволять пользователю выйти из программы.


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()


#search by Wikipedia
def search_Wiki(query):
    browser.get("https://www.wikipedia.org/")
    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    return browser.current_url

def get_page_content(url):
    #get page content
    browser.get(url)
    time.sleep(3)
    title = browser.find_element(By.ID, "firstHeading").text
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    
