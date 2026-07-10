import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
print(df.head())
print(df.shape)
df.info()
print(df.isna().sum())

df2 = df.drop(columns=["deck"])
df2['age'] = df2["age"].fillna(df2['age'].median())
df2 = df2.dropna(subset=["embarked"])
print(df2.isna().sum())
print(df2.groupby('who')['survived'].mean())

print(df2.groupby("pclass")["survived"].mean())
print(df2.groupby(["pclass","sex"])["survived"].mean())
print((df2.groupby("sex")["survived"].mean()))


sns.barplot(data=df2, x="pclass", y="survived", hue="sex")
plt.savefig('barplot.png', dpi=100, bbox_inches='tight')
plt.close()
sns.boxplot(data=df2, x="survived", y="age")
plt.savefig('boxplot.png', dpi=100, bbox_inches='tight')
plt.close()
sns.histplot(df2["fare"])
plt.savefig('histplot.png', dpi=100, bbox_inches='tight')
plt.close()


