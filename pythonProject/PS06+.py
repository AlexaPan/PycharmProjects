from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("URL_ВАШЕГО_САЙТА")  # Замените на URL вашего сайта

try:
    # Ожидание появления элементов с классом 'products-view-item'
    shelving = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'products-view-item'))
    )

    print(f"Найдено элементов: {len(shelving)}")

    # Выбор третьего элемента (индекс 2)
    rack = shelving[2]
    print(f"Текст элемента: {rack.text}")
    print(f"HTML элемента: {rack.get_attribute('outerHTML')}")

    # Прокрутка до элемента
    driver.execute_script("arguments[0].scrollIntoView();", rack)

    # Наведение курсора на элемент
    actions = ActionChains(driver)
    actions.move_to_element(rack).pause(1).perform()

    # Ожидание появления размеров
    sizes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-view-body-size__item'))
    )

    print(f"Найдено размеров: {len(sizes)}")
    if sizes:
        for size in sizes:
            print(f"Размер: {size.text}")
    else:
        print("Размеры не найдены.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()