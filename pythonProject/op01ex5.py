#converter
def currency_converter():
    # Установим курсы валют
    exchange_rates = {
        'USD': 102.0,  # курс рубля к доллару
        'EUR': 106.0,  # курс рубля к евро
        'CNY': 13.5   # курс рубля к юаню
    }

    print("Добро пожаловать в конвертер валют!")
    rubles = float(input("Введите сумму в рублях: "))

    print("Выберите валюту для конвертации:")
    print("1. Доллар (USD)")
    print("2. Евро (EUR)")
    print("3. Юань (CNY)")

    choice = input("Введите номер валюты (1/2/3): ")

    if choice == '1':
        converted_amount = rubles / exchange_rates['USD']
        print(f"{rubles} рублей = {converted_amount:.2f} долларов")
    elif choice == '2':
        converted_amount = rubles / exchange_rates['EUR']
        print(f"{rubles} рублей = {converted_amount:.2f} евро")
    elif choice == '3':
        converted_amount = rubles / exchange_rates['CNY']
        print(f"{rubles} рублей = {converted_amount:.2f} юаней")
    else:
        print("Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")

# Запускаем конвертер
currency_converter()
