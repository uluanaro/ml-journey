import sqlite3
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
conn = sqlite3.connect(':memory:')
df.to_sql('titanic', conn, index=False, if_exists='replace')

def q(sql):
    return pd.read_sql(sql, conn)
print(df.columns.tolist())

print(q("SELECT * FROM titanic LIMIT 5"))

print(q("SELECT pclass, AVG(survived), COUNT(*) "
        "FROM titanic "
        "GROUP BY pclass "
        "ORDER BY pclass"))

print(q("SELECT pclass, sex, AVG(age), AVG(fare) "
        "FROM titanic GROUP BY pclass, sex "
        "ORDER BY pclass"))

print(q("SELECT pclass, fare, AVG(fare) OVER (PARTITION BY pclass) "
        "FROM titanic "
        "LIMIT 10"))

df["family_size"] = df["sibsp"] + df["parch"] + 1
df["is_alone"] = (df["family_size"] == 1).astype(int)
df = pd.get_dummies(df, columns=['sex', 'embarked'])
df["age_bin"] = pd.cut(df["age"], bins=[0, 12, 18, 60, 100], labels=["child", "teenager", "adult", "senior"])
print(df.groupby("is_alone")["survived"].mean())