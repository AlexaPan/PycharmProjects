import pandas as pd

# Чтение данных из файла prices.csv
df = pd.read_csv('prices.csv')

# Предполагая, что в файле есть колонка с ценами, назовем её 'price'
# Удаляем 'руб.' из значений в колонке 'price'
df['price'] = df['price'].str.replace('руб.', '').str.strip()

# Удаляем пробелы и заменяем запятую на точку
df['price'] = df['price'].str.replace(' ', '').str.replace(',', '.')

# Удаляем пустые строки
df = df.dropna(subset=['price'])

# Преобразуем значения в колонке 'price' в числовой формат
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Удаляем строки с NaN после преобразования
df = df.dropna(subset=['price'])

# Сохраняем обновленные данные обратно в файл
df.to_csv('prices.csv', index=False)

print("Значение 'руб.' успешно удалено, пробелы убраны, пустые строки убраны, и значения преобразованы в числа в файле prices.csv.")
