#op04 ex1
"""
def start_range(start, end):
    sum = 0
    if start < end:
        for i in range(int(start//1), int((end+1)//1)):
            sum+=i
        return sum
    else:
        return None

start_value = ""
end_value = ""
while not (start_value.isdigit() and end_value.isdigit()):
    start_value = input((f"Enter start value "))
    end_value= input((f"Enter end value "))
print(f"Sum = {start_range(int(start_value), int(end_value))}")


#op4ex2
import math

def square_box(side):
    tuple_squre = (4*side, side*side, math.sqrt(2)*side)
    return tuple_squre

side = ""
while not (side.isdigit()):
    side = input((f"Enter side of square "))
side = int(side)
tuple_square = square_box(side)
print(f"Perimeter = {tuple_square[0]}, Square = {tuple_square[1]}, "
      f"Diagpnal = {tuple_square[2]}")
"""

#op4ex3

def bank(deposit, years):
    deposit_after = deposit
    for i in range(years):
       deposit_after += deposit_after*0.1
    return deposit_after

deposit = ""
while not deposit.isdigit():
    deposit = input((f"Enter deposite "))
deposit = float(deposit)

year = ""
while not year.isdigit():
    year = input((f"Enter number of years "))
year = int(year)

print(f"Deposit after {year} years is {bank(deposit, year)}")


