"""

#ex 1
def safe_divide(a, b):
    try:
        result_division = a/b
        return result_division
    except ZeroDivisionError:
        return None


a = float(input(f"Enter number one: "))
b = float(input(f"Enter number two: "))
res = safe_divide(a, b)
print(f"Result = {res}")

#ex 2
while True:
    try:
        int_num = int(input(f"Enter the <int> value: "))
    except (TypeError, ValueError) as a_error:
        print(a_error)
        print("Let's try again")
    else:
        print(f"The result = {int_num}")
        break
"""

#ex 3
#Возьми одну из программ, которую мы писали на прошлых уроках, продумай,
#какие ошибки в программе могут появляться(можно прям специально пробовать
#ее ломать) и дополни код конструкцией try-except для обработки выявленных исключений.

def safe_divide(a, b):
    try:
        result_division = a/b
        return result_division
    except ZeroDivisionError:
        return None


while True:
    try:
        a = float(input(f"Enter number one: "))
        b = float(input(f"Enter number two: "))
    except Exception as you_error:
        print(you_error)
        print("Let's try again\n")
    else: break

res = safe_divide(a, b)
print(f"Result = {res}")