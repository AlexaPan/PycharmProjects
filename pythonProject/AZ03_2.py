# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.​
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import matplotlib.pyplot as plt
import numpy as np

# Данные
y = np.random.rand(5)
x = np.random.rand(5)

# Создание графика
plt.scatter(x, y)
plt.title("Scatter plot for random data")
plt.xlabel("Axis X")
plt.ylabel("Axis Y")
plt.show()