"""

#exersize 1
listnum = []
for i in range(3):
    num = float(input(f"Enter num {i+1} "))
    listnum.append(num)
min_num = listnum[0]
for i in range(3-1):
    if listnum[i]<listnum[i+1]:
        min_num = listnum[i]
    else:
        min_num = listnum[i+1]
print(f"Min num = {min_num}")


#exersize 2
print("This program calculates the sum or difference or multiplication or division for two numbers")
number_1 = float(input(f"Enter the first number <a> "))
number_2 = float(input(f"Enter the second number <b> "))
operator = input(f"Enter operation sign + or - or * or / ")
match operator:
    case "+":
        print(f"a{operator}b={number_1 + number_2} ")
    case "-":
        print(f"a{operator}b={number_1 - number_2} ")
    case "*":
        print(f"a{operator}b={number_1 * number_2} ")
    case "/":
        if number_2 != 0:
            print(f"a{operator}b={number_1 / number_2} ")
        else:
            print(f"Division by zero")
    case _:
        print(f"Undefined operator")



#exersize 3
length_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
n = int(input(f"Enter the number of the month "))
l = length_month[n-1]
print(f"The length of the {n}th month is {l} days")



#exersize 4
beg_number = int(input(f"Enter an integer beginning of the range "))
end_number = int(input(f"Enter an integer end of the range "))
if beg_number < end_number:
    for i in range(beg_number, end_number):
        if (i % 2) == 0 and i != 0:
            print(f" {i} ")
else:
    print("Out of range")

"""

#exersize 5
import random
sub_tuple = ("stone", "scissors", "paper")
sub_list = ["1", "2", "3"]
win_my = 0
win_you = 0
while win_my != 3 or win_you != 3:
    your_choice = input(f"Your choice. Enter: 1 - stone, 2 - scissors, 3 - paper: ")
    print(f"{your_choice}")
    while not (your_choice.isdigit() and str(your_choice) in sub_list):
        print(f"Incorrect input: {your_choice}")
        your_choice = input(f"Your choice. Enter: 1 - stone, 2 - scissors, 3 - paper: ")
    your_choice = int(your_choice)
    my_choice = random.randint(1,3)
    print(f"My random choice is {sub_tuple[my_choice-1]}")
    if your_choice == 1 and my_choice == 1 or your_choice == 2 and my_choice == 2 or your_choice == 3 and my_choice == 3:
        print(f"Result: Drown game ")
    elif your_choice == 1 and my_choice == 3 or your_choice == 2 and my_choice == 1 or your_choice == 3 and my_choice == 2:
        print(f"Result: I won!")
        win_my +=1
    elif your_choice == 1 and my_choice == 2 or your_choice == 2 and my_choice == 3 or your_choice == 3 and my_choice == 1:
        print(f"Result: You won!")
        win_you +=1
if win_my == 3:
    print("I won three times")
else:
    print("You won three times")