# Предтавьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# - можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонениес
from dataclasses import replace

import pandas as pd
import numpy as np

df = pd.read_csv("grades.csv")

def stat_df(df):
    # Проверка на пустой DataFrame
    if df.empty:
        return pd.DataFrame()  # Возвращаем пустой DataFrame
    df_new = df.copy()
    # Вычисление статистических показателей
    # ather way to calculate mean
    subject_mean_ather = df.iloc[:, 1:].mean(axis=0, skipna=True)
    subject_median_ather = df.iloc[:, 1:].median(axis=0, skipna=True)
    subject_std_ather = df.iloc[:, 1:].std(axis=0, skipna=True)
    subject_Q025_ather = df.iloc[:, 1:].quantile(0.25, axis=0)
    subject_Q075_ather = df.iloc[:, 1:].quantile(0.75, axis=0)
    subject_IQR_ather = subject_Q075_ather - subject_Q025_ather

    df_new.loc["Average"] = ["Average"] + subject_mean_ather.tolist()
    df_new.loc["Median"] = ["Median"] + subject_median_ather.tolist()
    df_new.loc["Std"] = ["Std"] + subject_std_ather.tolist()
    df_new.loc["Q025"] = ["Q025"] + subject_Q025_ather.tolist()
    df_new.loc["Q075"] = ["Q075"] + subject_Q075_ather.tolist()
    df_new.loc["IQR"] = ["IQR"] + subject_IQR_ather.tolist()
    print(df_new)


def replace_outliers(df):
    if df.empty:
        return df

    df_numeric = df.select_dtypes(include=[np.number])
    IQR = df_numeric.quantile(0.75) - df_numeric.quantile(0.25)
    downside = df_numeric.quantile(0.25) - 1.5 * IQR
    upside = df_numeric.quantile(0.75) + 1.5 * IQR

    for col in df_numeric.columns:
        df[col] = df[col].where((df[col] >= downside[col]) &
                                (df[col] <= upside[col]),  other=pd.NA)

    #df_new = df.dropna(axis=0, how='any')
    return df


print(df.head())

print(df.describe())

subject_mean = {}
for subject in df.columns[1:]:
    subject_mean[subject] = df[subject].mean(skipna=True)
    print(f"Mean grade on {subject}: {subject_mean[subject]}")

stat_df(df)

Q025 = df['Mathematics'].quantile(0.25)
Q075 = df['Mathematics'].quantile(0.75)
IQR = Q075 - Q025

#eliminate outliers in the Data
downside = Q025 - 1.5 * IQR
upside = Q075 + 1.5 * IQR
print(f"For Mathematics: Q025: {Q025}, Q075: {Q075}, IQR: {IQR}, downside is: {downside}, upside is: {upside}")

df_new = replace_outliers(df)
print(f"New DataFrame with replaced to NaN outliers:\n{df_new}\n")  # Print the new DataFrame without outliers (df_new)
stat_df(df_new.tail())

print("You can see the result of statistics in the DataFrame if the outliers are changed to NaN. \n "
      "It's changed from the statistics of the original DataFrame")
