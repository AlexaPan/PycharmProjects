import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def status(self):
        return f"{self.name}: здоровье = {self.health}"

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

    def player_turn(self):
        print("\nХод игрока:")
        self.player.attack(self.computer)
        print(self.computer.status())

    def computer_turn(self):
        print("\nХод компьютера:")
        self.computer.attack(self.player)
        print(self.player.status())

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()