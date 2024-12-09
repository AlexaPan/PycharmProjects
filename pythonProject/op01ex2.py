#what's your name
first_name = input (" Enter yor first name ")
last_name = input(" Enter your last name ")
age = int(input(" Enter your age "))
# Вычисляем месяцы, часы и минуты
months = age * 12
hours = age * 365 * 24  # учитываем, что в году 365 дней
minutes = hours * 60

# Выводим информацию на экран
print(f"Your first name is {first_name} \nYour last name is {last_name}")
print(f"You are {age} years old.")
print(f"That's approximately {months} months, {hours} hours, or {minutes} minutes.")