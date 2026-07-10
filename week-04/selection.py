# import pandas as pd
#
# df = pd.DataFrame({
#     'name': ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena'],
#     'age': [25, 40, 30, 35, 28],
#     'income': [50000, 80000, 60000, 75000, 55000],
#     'city': ['Moscow', 'Kazan', 'Moscow', 'Kazan', 'Moscow']
# })
# print(df)
# print(df['age'])
# print(df[['age', 'city']])
# print(df[["name"]])
# print(type(df[["name"]]))
# print("------------------")
# print(df.iloc[1])
#
#
# df2 = df.set_index("name")
# print(df2)
# print(df2.loc["Elena"])
# print("------------------")
# print(df[df["income"] > 60000])
#
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     'name':   ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena'],
#     'age':    [25, np.nan, 30, 35, np.nan],
#     'income': [50000, 80000, np.nan, 75000, 55000],
#     'city':   ['Moscow', 'Kazan', 'Moscow', np.nan, 'Moscow']
# })
# print(df)
# print(df.isna())
# print(df.isna().sum())
# print(df.dropna())
# print(df["age"].fillna(df["age"].mean()))
# print(df.duplicated())
# print(df.drop_duplicates())
# print(df['income'].apply(lambda x: x/1000))

import pandas as pd
import numpy as np

# 1. Создаём данные (один раз)
df = pd.DataFrame({
    'name':   ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena'],
    'age':    [25, np.nan, 30, 35, np.nan],
    'income': [50000, 80000, np.nan, 75000, 55000],
    'city':   ['Moscow', 'Kazan', 'Moscow', np.nan, 'Moscow']
})

# 2. Смотрим, где пропуски
print("Пропуски до чистки:")
print(df.isna().sum())

# 3. Заполняем осмысленно и СОХРАНЯЕМ обратно
df['age'] = df['age'].fillna(df['age'].mean())         # возраст - средним
df['income'] = df['income'].fillna(df['income'].median())  # доход - медианой
df['city'] = df['city'].fillna('Unknown')              # город - константой

# 4. Проверяем, что дырок не осталось
print("\nПропуски после чистки:")
print(df.isna().sum())
print("\nИтоговая таблица:")
print(df)


#GROUPBY
df = pd.DataFrame({
    'name':   ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena', 'Fedor'],
    'age':    [25, 40, 30, 35, 28, 45],
    'income': [50000, 80000, 60000, 75000, 55000, 90000],
    'city':   ['Moscow', 'Kazan', 'Moscow', 'Kazan', 'Moscow', 'Kazan']
})
print(df)
print(df.groupby('city')["income"].mean())
print(df.groupby("city")["income"].max())

print(df.groupby("city")["income"].count())
print(df.groupby("city")["income"].min())

print(df.groupby('city')["age"].mean())
