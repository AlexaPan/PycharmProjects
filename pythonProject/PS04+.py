from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка ChromeDriver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
# chrome_service = Service('C:/path/to/chromedriver.exe')  # Укажите правильный путь

# Инициализация драйвера
driver = webdriver.Chrome()

def search_wikipedia(query):
    """Поиск статьи на Википедии."""
    driver.get("https://www.wikipedia.org")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)  # Нажатие Enter для поиска
    time.sleep(2)  # Ожидание загрузки страницы
    return driver.current_url

def get_page_content(url):
    """Получение содержимого страницы."""
    driver.get(url)
    time.sleep(2)  # Ожидание загрузки страницы

    try:
        # Ожидание загрузки заголовка статьи
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        title = driver.find_element(By.ID, "firstHeading").text

        # Ожидание загрузки параграфов
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mw-parser-output']//p"))
        )
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='mw-parser-output']//p")
        content = [p.text for p in paragraphs if p.text.strip()]

        # Получение связанных страниц
        links = driver.find_elements(By.XPATH, "//div[@class='mw-parser-output']//a[contains(@href, '/wiki/')]")
        link_titles = [link.text for link in links if link.text.strip()]

        return title, content, link_titles
    except Exception as e:
        print(f"Ошибка при получении содержимого страницы: {e}")
        return None, [], []

def display_paragraphs(content):
    """Отображение параграфов."""
    if not content:
        print("Параграфы не найдены.")
        return

    for i, paragraph in enumerate(content):
        print(f"\nПараграф {i + 1}:")
        print(paragraph)
        input("\nНажмите Enter для продолжения...")

def display_links(links):
    """Отображение связанных страниц."""
    if not links:
        print("Связанные страницы не найдены.")
        return []

    print("\nСвязанные страницы:")
    for i, title in enumerate(links[:10]):  # Ограничиваем вывод 10 ссылками
        print(f"{i + 1}. {title}")
    return links[:10]

def main():
    print("Добро пожаловать в поисковик Википедии!")
    query = input("Введите ваш запрос: ")
    url = search_wikipedia(query)

    if not url:
        print("Статья не найдена.")
        return

    while True:
        title, content, links = get_page_content(url)
        if not title:
            print("Не удалось получить содержимое страницы.")
            break

        print("\nТекущая статья:", title)
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == "1":
            display_paragraphs(content)
        elif choice == "2":
            displayed_links = display_links(links)
            if displayed_links:
                link_choice = input("Введите номер связанной страницы: ")
                try:
                    link_choice = int(link_choice) - 1
                    if 0 <= link_choice < len(displayed_links):
                        link_title = displayed_links[link_choice]
                        url = f"https://en.wikipedia.org/wiki/{link_title.replace(' ', '_')}"
                    else:
                        print("Неверный номер.")
                except ValueError:
                    print("Введите число.")
            else:
                print("Нет связанных страниц.")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    driver.quit()

if __name__ == "__main__":
    main()