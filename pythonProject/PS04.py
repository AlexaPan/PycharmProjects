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
    time.sleep(1)
    return browser.current_url

def hatnotes_print(browser, url):


    hatnotes = []
    contents_w = []
    links = []
    titles = []
    contents = []
    try:
        browser.get(url)
        time.sleep(1)
        for element in browser.find_elements(By.TAG_NAME, "div"):
            # Чтобы искать атрибут класса
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading" or cl =="mw-body-content":
                hatnotes.append(element)
            if cl =="mw-body-content":
                contents_w.append(element)

        for i, hatnote in enumerate(hatnotes[:10]):
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            links.append(link)
            title = hatnote.find_element(By.TAG_NAME, "a").get_attribute("title")
            titles.append(title)
            print(f"Link {i+1} {title}: {link}")

        for i, content_w in enumerate(contents_w[:10]):
            content = content_w.find_element(By.TAG_NAME, "p").text
            if content.strip():
                contents.append(content)
            print(f"\nContent {i + 1} {titles[i]}: {content}")

        return titles, contents, links

    except Exception as e:
        print(f"Error getting page content: {e}")
        return [], [], []



#get page content, paragraphs
def get_page_content(browser, url):

    try:
        browser.get(url)
        time.sleep(1)
        title = browser.find_element(By.ID, "firstHeading").text
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        content = [p.text for p in paragraphs if p.text.strip()] #create list of paragraphs

        all_links = browser.find_elements(By.TAG_NAME, "a")

        # Filter links, excluding service links and files
        links = []
        for link in all_links:
            href = link.get_attribute("href")
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
        print(f"Paragraph {i+1}:\n{paragraph}")
        input("Enter for continue...")

def print_links(links):
    if not links:
        print("Links not found.")
        return

    for i, link in enumerate(links[:10]): #only first 10 links printed
        print(f"Link {i+1}: {link.get_attribute("href")}")

    return links[:10]

def main_loop():
    browser = driver_init()
    print("Use Wiki search!")

    while True:
        query = input("Enter the search request: ")
        url = search_Wiki(browser, query)

        if not url:
            print("The article not found.")
            return

        while True:
            #title, content, links = get_page_content(browser, url)
            title_h, content_h, links_h = hatnotes_print(browser, url)

            if not title_h:
                print("The article might has no title")
                time.sleep(3)
                break


            print(f"\n Current article: {title_h}")
            print("Choose: "
                  "\n 1 - Show paragraph."
                  "\n 2 - Go to the link."
                  "\n 3 - Exit.")

            choice = "0"
            while choice not in ["1", "2", "3"]:
                choice = input("Your choice: ").strip()

            if choice == "1":
                print_paragraph(content_h)

            if choice == "2":
                links_10 = print_links(links)
                if links_10:
                    link_choice = input("Enter the link's number: ")
                    try:
                        link_index = int(link_choice) - 1
                        if 0 <= link_index < len(links_10):
                            url = links_10[link_index].get_attribute("href")  # переход на выбранную ссылку
                        else:
                            print("Invalid link number.")
                    except ValueError:
                        print("Please enter a valid number.")

            if choice == "3":
                browser.quit()
                return None




main_loop()













    
