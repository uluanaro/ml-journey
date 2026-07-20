import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("telco.csv")

print(df.head())
print(df.info())
print(df.columns.tolist())
print(df.shape)

df["Churn_num"] = (df["Churn"] == "Yes").astype(int)
print(df.groupby("gender")["Churn_num"].mean())
print(df.groupby("PaymentMethod")["Churn_num"].mean())


print((df["TotalCharges"] == " ").sum())
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print(df["TotalCharges"].dtype)
print(df["TotalCharges"].isna().sum())
df.dropna(subset=["TotalCharges"], inplace=True)
print(df.shape)
print(df.duplicated().sum())
df2 = df.drop(columns=["customerID"])
print(df2.shape)

sns.histplot(df2["tenure"])
plt.savefig("tenure.png", dpi=100, bbox_inches='tight')
plt.close()
sns.histplot(df2["MonthlyCharges"])
plt.savefig("monthly_charges.png", dpi=100, bbox_inches='tight')
plt.close()
sns.histplot(df2["TotalCharges"])
plt.savefig("total_charges.png", dpi=100, bbox_inches='tight')
plt.close()


print(df2.groupby("Contract")["Churn_num"].mean())
bins = pd.cut(df2["tenure"], bins=5, labels=False)
print(df2.groupby(bins)["Churn_num"].mean())

cols = df2[["tenure", "MonthlyCharges", "TotalCharges", "Churn_num"]]
corr_matrix = cols.corr()
sns.heatmap(corr_matrix, annot=True)
plt.savefig("corr.png", dpi=100, bbox_inches='tight')
plt.close()

bins2= pd.cut(df2["MonthlyCharges"], bins=2, labels=False)
print(df2.groupby(bins2)["Churn_num"].mean())


df2["tenure_group"] = pd.cut(df2["tenure"], bins=[0, 12, 24, 48, 72],
                             labels=["новичок", "средний", "лояльный", "ветеран"])
print(df2.groupby("tenure_group")["Churn_num"].mean())
df2["is_month_to_month"] = (df2["Contract"] == "Month-to-month").astype(int)
print(df2.groupby('is_month_to_month')["Churn_num"].mean())
df2 = df2.drop(columns=["TotalCharges"])
df2 = pd.get_dummies(df2, columns=["Contract", "PaymentMethod", "InternetService"])
print(df2.shape)