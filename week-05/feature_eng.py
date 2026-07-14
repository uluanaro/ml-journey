import pandas as pd
import seaborn as sns

df  = sns.load_dataset("titanic")
print(df[["survived", 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']].head())

print(pd.get_dummies(df['sex'], drop_first = True))

df['family_size'] = df['sibsp']+df['parch'] + 1
print(df['family_size'])
df['is_alone'] = (df['family_size'] == 1).astype(int)
print(df['is_alone'])
print(pd.cut(df['age'], bins = [0, 12, 18, 60, 100], labels = ['child', 'teenager', 'adult', 'senior']))