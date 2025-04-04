# Разработать консольную игру "Битва героев" на Python с использованием классов и разработать
# план проекта по этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 2. Игра должна быть реализована как консольное приложение.
# Классы:
# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

#from abc import ABC, abstractmethod
import random

# class HeroAbstract(ABC):
#     @abstractmethod
#     def info(self):
#         pass


class Hero():
    def __init__(self, name, health=100, attack_power=20, defense_power=10, speed = None,
                 critical_chance = None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.speed = speed if speed is not None else random.randint(1, 7)
        self.critical_chance = critical_chance if critical_chance is not None else random.randint(1, 10)
        print(self.info())

    def attack(self, other):
        attack_damage = self.attack_power+random.randint(-5, 5)+self.defense_power-random.randint(0, other.critical_chance)
        other.health -= attack_damage
        print(f"{self.name} attacks {other.name} for {attack_damage} damage. \n{other.name} has {other.health} health left.\n")



    def is_alive(self):
        return self.health > 0

    def info(self):
        return f"{self.name}:\n health = {self.health},\n attack power = {self.attack_power},\n defense power = {self.defense_power},\n speed = {self.speed},\n critical chance = {self.critical_chance}"

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Game started!\n")
        who_is_first = (self.player.speed >= self.computer.speed)

        while self.player.is_alive() and self.computer.is_alive():
            if who_is_first:
                self.player.attack(self.computer)
            who_is_first = True

            if not self.computer.is_alive():
                print(f"{self.player.name} wins!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} wins!")
                break

        if not self.player.is_alive() and not self.computer.is_alive():
            print("It's a draw!")

def initializeGame():
    player_name = input("Enter your name: ")
    player = Hero(player_name)
    computer_name = "Computer"
    computer_health = random.randint(50, 100)
    computer_attack_power = random.randint(10, 30)
    computer = Hero(computer_name, computer_health, computer_attack_power)
    game = Game(player, computer)
    game.start()

    while True:
        user_input = input("\nDo you want to play again? (yes/no): ")
        if user_input.lower() == "yes":
            initializeGame()
        elif user_input.lower() == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    initializeGame()

