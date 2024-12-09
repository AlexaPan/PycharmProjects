# *Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
#
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для items`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
#
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_items(self, name_item, price):
        self.items[name_item] = price
        print(f"\nItem {name_item} for store {self.name} added with price {price}")

    def remove_items(self, name_item):
        if name_item in self.items:
            print(f"\nItem {name_item} from store {self.name} removed")
            self.items.pop(name_item)  # удаляем элемент из словаря
        else:
            print(f"\nItem {name_item} in store {self.name} not found")

    def get_price(self, name_item):
        if name_item in self.items:
            print(f"\nPrice of {name_item} in store {self.name} is {self.items[name_item]}")
            return self.items[name_item]
        else:
            return None

    def update_price(self, name_item, new_price):
        if name_item in self.items:
            self.items[name_item] = new_price
            print(f"\nPrice of {name_item} in store {self.name} updated to {new_price}")
        else:
            print(F"\nItem {name_item} in store {self.name} not found")

    def print_items(self):
        print(f"\nStore: {self.name}")
        print(f"Address: {self.address}")
        print("Items:")
        for name, price in self.items.items():
            print(f"{name}: {price}")

if __name__ == "__main__":
    store = Store("My Store 1", "123 Main St")

    store.add_items("apple", 0.5)
    store.add_items("banana", 0.75)
    store.add_items("orange", 0.9)
    store.add_items("grape", 1.2)
    store.print_items()

    store.remove_items("apple")

    store.update_price("orange", 1.5)
    store.update_price("banana", 0.8)

    store.print_items()

    store02 = Store("My Store 2", "456 Market St")
    store02.add_items("milk", 2.5)
    store02.add_items("bread", 1.2)
    store02.add_items("eggs", 3.0)
    store02.add_items("cheese", 4.5)
    store02.print_items()

    store03 = Store("My Store 3", "789 Market St")
    store03.add_items("bread", 1.2)
    store03.add_items("eggs", 3.0)
    store03.add_items("cheese", 4.5)
    store03.print_items()

    store02.remove_items("eggs")

    store03.update_price("bread", 1.5)
    store03.update_price("cheese", 5.0)
    print(store03.get_price("bread"))

    store.print_items()
    store02.print_items()
    store03.print_items()