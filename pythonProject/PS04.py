# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# 4. Позволять пользователю выйти из программы.
from anyio import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time


# driver create
def driver_init():
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/")
    return browser

# search by Wikipedia
def search_Wiki(browser, query):
    search_box = browser.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    return browser.current_url

#get page content, paragraphs
def get_page_content(browser, url):
    browser.get(url)
    time.sleep(3)
    try:
        title = browser.find_element(By.ID, "firstHeading").text
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        content = [p.text for p in paragraphs if p.text.strip()] #create list of paragraphs

        all_links = browser.find_elements(By.TAG_NAME, "a")

        # Filter links, excluding service links and files
        links = []
        for link in all_links:
            href = link.get_attriute("href")
            if href and 'wiki/Служебная' not in href and 'wiki/Файл' not in href:
                links.append(link)
        return title, content, links

    except Exception as e:
        print(f"Error getting page content: {e}")
        return None, [], []

def print_paragraph(content):
    if not content:
        print("Paragraphs not found.")
        return
    for i, paragraph in enumerate(content):
        print(f"Paragraph {i}:\n{paragraph}")
        input("Enter for continue...")

def print_links(links):
    if not links:
        print("Links not found.")
        return

    for i, link in enumerate(links[:10]): #only first 10 links printed
        print(f"Link {i}: {link}")

    return links[:10]

def main_loop():
    print("Use Wiki search!")
    query = input("Enter the search request: ")
    url = search_Wiki(query)

    if not url:
        print("The article not found.")
        return

    while True:
        title, content, links = get_page_content(url)

        if not title:
            print("The article might has no title")
            sleep(3)
            break

        print(f"\n Current article: {title}")
        print("Choose: "
              "\n 1 - Show paragraph."
              "\n 2 - Go to the link."
              "\n 3 - Exit.")

        choice = "0"
        while choice not in ["1", "2", "3"]:
            choice = input("Your choice: ").strip()

        if choice == "1":
            print_paragraph(content)

        if choice == "2":
            links_10 = print_links(links)
            if links_10:
                link_choice = input("Enter the link's number: ")

        if choice == "3":
            break












    
