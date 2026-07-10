import pandas as pd

df = pd.DataFrame({
    'name': ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena'],
    'age': [25, 40, 30, 35, 28],
    'income': [50000, 80000, 60000, 75000, 55000],
    'city': ['Moscow', 'Kazan', 'Moscow', 'Kazan', 'Moscow']
})

print(df)
print("---")
print(df.shape)      # форма таблицы
print(df.dtypes)     # тип КАЖДОГО столбца
print(df.columns)    # имена столбцов
print(df.head(3))     # первые 3 строки — "как выглядят данные"
print("---")
print(df.info())      # сводка: сколько строк, типы, сколько НЕ пустых
print("---")
print(df.describe())  # статистика по ЧИСЛОВЫМ столбцам