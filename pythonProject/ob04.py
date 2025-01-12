# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
#
# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.
#
# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости:
# новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
#
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, name, monster):
        pass


class Sword(Weapon):
    def attack(self, fighter_name, monster):
        print(f"The {fighter_name} attacks with a sword.")
        damage(self, monster, 50)

class Bow(Weapon):
    def attack(self, fighter_name, monster):
        print(f"The {fighter_name} attacks with a bow.")
        damage(self, monster, 30)

class Mace(Weapon):
    def attack(self, fighter_name, monster):
        print(f"The {fighter_name} attacks with a mace.")
        damage(self, monster, 40)




class Fighter:
    def __init__(self, fighter_name, weapon: Weapon, health=100):
        self.name = fighter_name
        self.weapon = weapon
        self.health = health

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"The fighter {self.name} changes their weapon to {weapon.__class__.__name__}.")

    def attack(self, monster):
        self.weapon.attack(self.name, monster)



class Monster:
    def __init__(self, monster_name):
        self.name = monster_name
        self.health = 100

    def attack(self, fighter):
        print(f"{self.name} attacks!")
        damage(self, fighter, 30)


def damage(self, battler, damage):
    if battler.health <= 0:
        print(f"{battler.name} is already defeated!")
        return
    battler.health -= damage
    if battler.health > 0:
        print(f"{battler.name} is damaged!")
    else:
        print(f"{battler.name} is defeated!")





fighter = Fighter("John", Sword())
monster = Monster("Goblin")

fighter.attack(monster)
monster.attack(fighter)
fighter.change_weapon(Bow())
fighter.attack(monster)
fighter.change_weapon(Mace())
fighter.attack(monster)
fighter.attack(monster)
