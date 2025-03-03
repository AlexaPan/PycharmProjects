# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv(r"C:\Users\Mysh\Downloads\archive\cleaned_speakers_data.csv")
print("First 5 rows in df:")
print(df.head(5))
input("Press enter to continue...\n")

print("Data info:")
print(df.info())
input("Press enter to continue...\n")

print("Statistics:")
print(df.describe())
input("Press enter to continue...\n")

df_city = pd.read_csv(r"C:\Users\Mysh\Downloads\dz.csv")
print(df_city)
print("\nAverage salary by city:\n")

df_city.dropna(inplace=True)

print(df_city.groupby("City")["Salary"].mean())
