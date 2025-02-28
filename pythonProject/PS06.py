import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
url = "https://kinash.ru/categories/krossovki"
driver.get(url)

# Создаем объект ActionChains
actions = ActionChains(driver)

try:
    # Ожидание появления элементов с классом 'products-view-item'
    arg_shelving = (By.CLASS_NAME, 'products-view-item')
    shelving = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(arg_shelving)
    )

    print(f"Найдено элементов: {len(shelving)}")
    parsed_data = []
    count = 0
    for count, rack in enumerate(shelving, start=1):
        try:

            print(f"Parsing of {count}")
            # Получение названия и ссылки
            title = rack.find_element(By.CSS_SELECTOR, '.products-view-name-link').text
            link = rack.find_element(By.CSS_SELECTOR, '.products-view-name-link').get_attribute('href')

            # Прокрутка до элемента
            driver.execute_script("arguments[0].scrollIntoView();", rack)
            time.sleep(1)  # Небольшая задержка для прокрутки

            # Наведение курсора на элемент
            actions.move_to_element(rack).pause(1).perform()
            time.sleep(1)  # Небольшая задержка для прокрутки

                # Ожидание появления размеров
            try:
                sizes_web = WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-view-body-size__item'))
                )
                sizes = [size.text for size in sizes_web if size.text.strip()]
                print(sizes)
            except Exception as e:
                sizes = []
                print(f"Произошла ошибка при парсинге цен элемента {count}: {e}")


            # Получение цены
            try:
                price = rack.find_element(By.CSS_SELECTOR, '.price-number').text
            except:
                price = "Not specified"

            # Добавление данных в список
            parsed_data.append([title, price, link, ", ".join(sizes)])
            #parsed_data.append([title, price, link])
        except Exception as e:
            print(f"Ошибка при парсинге элемента: {e}")
            continue

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()

# Запись данных в CSV-файл
with open("kinash.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Link', 'Sizes'])
    #writer.writerow(['Name', 'Price', 'Link'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в файл 'kinash.csv'.")