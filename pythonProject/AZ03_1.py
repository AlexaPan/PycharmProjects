# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения
# mean = 0 # Среднее значение
# std_dev = 1 # Стандартное отклонение
# num_samples = 1000 # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import matplotlib.pyplot as plt
import numpy as np

# Данные
data = np.random.normal(0, 1, 1000)

# Создание графика
plt.hist(data, bins=20, edgecolor='black')
plt.title("Histogram of normal distribution for random data")
plt.xlabel("Axis X")
plt.ylabel("Axis Y")
plt.show()