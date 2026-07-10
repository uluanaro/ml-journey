import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'age': np.random.randint(22, 60, 100),
    'salary': np.random.normal(70000, 20000, 100),
    'experience': np.random.randint(0, 30, 100),
    'dept': np.random.choice(['IT', 'Sales', 'HR'], 100)
})
df.loc[0, 'salary'] = 250000

sns.histplot(df['salary'])
plt.show()
sns.scatterplot(data=df, x='experience', y='salary')
plt.show()
sns.boxplot(data=df, x='salary')
plt.show()
df2 = df.corr(numeric_only=True)
sns.heatmap(df2, annot=True)
plt.show()