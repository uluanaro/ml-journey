import pandas as pd
import numpy as np
#
# df = pd.DataFrame({
#     'name':   ['Anna', 'Boris', 'Vera', 'Dmitry', 'Elena', 'Fedor'],
#     'age':    [25, np.nan, 30, 35, 28, np.nan],
#     'salary': [50000, 80000, np.nan, 75000, 55000, 90000],
#     'dept':   ['IT', 'Sales', 'IT', 'Sales', 'IT', 'Sales']
# })
# print(df)
# #print(df.isna().sum())
# df["age"] = df["age"].fillna(df["age"].median())
# df["salary"] = df["salary"].fillna(df["salary"].mean())
# print(df)
#
# print(df[(df["age"] > 28) & (df["dept"] == "IT")])
# print(df.iloc[3])
# print(df.groupby("dept")["salary"].mean())

#merge

employees = pd.DataFrame({
    'name': ['Anna', 'Boris', 'Vera', 'Dmitry'],
    'dept_id': [1, 2, 1, 3]
})

departments = pd.DataFrame({
    'dept_id': [1, 2, 4],
    'dept_name': ['IT', 'Sales', 'HR']
})

print(pd.merge(employees, departments,on="dept_id", how='inner'))
print(pd.merge(employees, departments,on="dept_id", how='left'))
print(pd.merge(employees, departments,on="dept_id", how='outer'))