# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
# о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было
# "постоянное состояние" между запусками программы.

import json

class Animal:
    def __init__(self, name, age, voice):
        self.name = name
        self.age = age
        self.voice = voice
        print(f"Parent {self.name} was created")

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")
#        pass

    def eat(self):
        return f"{self.name} is eating"

class Bird(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
#        print(f"Child {self.name} was created")

    def make_sound(self):
        print(f"I'm a bird, I say '{self.voice}'")

    def eat(self):
        print("I'm a bird, I eat worms")

class Mammal(Animal):
    def make_sound(self):
        print(f"I'm a cat, I say '{self.voice}'")

    def eat(self):
        print("I'm a cat, I eat meat")

class Reptile(Animal):
    def make_sound(self):
        print(f"I'm a snake, I say '{self.voice}'")

    def eat(self):
        print("I'm a snake, I eat insects")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.zookeepers = []
        self.veterinarians = []

    def add_animal(self, zoo_animal):
        self.animals.append(zoo_animal)

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def add_veterinarian(self, veterinarian):
        self.veterinarians.append(veterinarian)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, zoo_animal):
        print(f"{self.name} feed {zoo_animal.name} for a day")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, zoo_animal):
        print(f"{self.name} heal {zoo_animal.name} for a day")

def print_zoo_info(zoo):
    print(f"Zoo name: {zoo.name}")
    print(f"The zoo has following employees: ")
    print(f"Zookeepers: ")
    for zookeeper in zoo.zookeepers:
        print(f"\t{zookeeper.name}")
    print(f"Veterinarians: ")
    for veterinarian in zoo.veterinarians:
        print(f"\t{veterinarian.name}")

def animal_sound(new_zoo):
    print("Animal sound in zoo:")
    for animal in new_zoo.animals:
        print("\t", end = '')
        animal.make_sound()

def animal_eat(new_zoo):
    print("Animal eat in zoo:")
    for animal in new_zoo.animals:
        print(f"\t", end = '')
        animal.eat()

def save_zoo(zoo, filename = 'zoo_data.json'):
    data = {
        'name': zoo.name,
        'animals': [
            {
            'type': animal.__class__.__name__,
            'name': animal.name,
            'age': animal.age,
            'voice': animal.voice
        }
        for animal in zoo.animals
        ], #Create key 'animals' and list of dictionaries
        'zookeepers': [
            {
            'zookeeper_name': zookeeper.name
            }
            for zookeeper in zoo.zookeepers
        ],
        'veterinarians': [
            {
            'veterinarian_name': veterinarian.name
            }
            for veterinarian in zoo.veterinarians
        ]
    }

    with open(filename, 'w') as f:
        json.dump(data, f)

def load_zoo(filename = 'zoo_data.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            zoo = Zoo(data['name'])

            for animal_data in data['animals']: #Create list of animals
                if animal_data['type'] == 'Bird':
                    zoo.add_animal(Bird(animal_data['name'], animal_data['age'], animal_data['voice']))
                elif animal_data['type'] == 'Mammal':
                    zoo.add_animal(Mammal(animal_data['name'], animal_data['age'], animal_data['voice']))
                elif animal_data['type'] == 'Reptile':
                    zoo.add_animal(Reptile(animal_data['name'], animal_data['age'], animal_data['voice']))

            for zookeeper_data in data['zookeepers']: #Create list of zookeepers
                zoo.add_zookeeper(ZooKeeper(zookeeper_data['zookeeper_name']))

            for veterinarian_data in data['veterinarians']: #Create list of veterinarians
                zoo.add_veterinarian(Veterinarian(veterinarian_data['veterinarian_name']))

    except FileNotFoundError:
        print("File not found. Creating a new zoo.")
        zoo = Zoo("Limpopo Zoo")

    return zoo




new_zoo_created = load_zoo() #Create zoo
animal = Animal("Lion", 5, "Roar")
#animal.make_sound()
new_animal = Bird("Raven", 3, "Karr")
new_zoo_created.animals = [Bird("Parrot", 3, "Chirp"),
                   Mammal("Dog", 5, "Woof"), Reptile("Snake", 2, "Hiss")]
new_zoo_created.add_animal(new_animal)

new_zoo_created.zookeepers = [ZooKeeper("John"), ZooKeeper("Sally")]
new_zoo_created.veterinarians = [Veterinarian("Jane")]

print_zoo_info(new_zoo_created)
animal_sound(new_zoo_created)
animal_eat(new_zoo_created)

save_zoo(new_zoo_created) #Save zoo to file
#print(new_zoo_created.animals[1].name)





