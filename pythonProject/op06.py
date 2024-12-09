# ex 1
#Задание 1. Создание и запись в файл
from math import trunc

#Напишите скрипт, который запрашивает у пользователя текст,
#а затем записывает этот текст в файл user_data.txt.

"""
text = ""
print("You have to write anything for new_file.\n"
      " To finish typing, type: AND")
while True:
    line = input()
    if line.strip().upper() == "AND":
        print("Input complete")
        break
    else:
        text += line + "\n"
with open("user_data.txt", "w") as new_file:
    new_file.write(text)
    


#ex 2
#Задание 2. Создание модуля с функциями арифметики

# Создайте модуль arithmetic.py, который будет содержать 4 функции:
# сложение, вычитание, умножение и деление. Импортируйте модуль в
# другой файл Python и выполните каждую из функций с произвольными аргументами.

import arithmetic
a = arithmetic.float_input()
b = arithmetic.float_input()
arithmetic.sum(a, b)
arithmetic.diff(a, b)
arithmetic.mul(a, b)
arithmetic.div(a, b)

"""

#ex 3
#Задание 3. Случайный выбор элемента
# Напишите программу, которая эмулирует выбор без повторений:
# из списка учащихся класса программа случайным образом выбирает 5 уникальных имён,
# которые будут отвечать на уроке. Имена учащихся считываются заранее
# из входного списка и не должны повторятся.

import random

my_list = ["Ann", "Kate", "Alex", "Sema", "Jack", "Robert", "Bob", "Vika", "Will", "Antony"]
list = my_list
print(my_list)
print("Today they answer: ")
for i in range(1, 6):
    Name = random.choice(list)
    list.remove(Name)
    print(Name)
