import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из файла prices.csv
df = pd.read_csv('prices.csv')

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=10, color='blue', alpha=0.7)
plt.title('Гистограмма цен с сайта divan.ru')
plt.xlabel('Цена')
plt.ylabel('Частота')

x_ticks = np.linspace(min(df['price']), max(df['price']), 11) # Установите нужное количество точек

plt.xticks(x_ticks)
# Включаем основную и вспомогательную сетку по всем осям
plt.grid(which='both', axis='both', alpha=0.75)
plt.show()
