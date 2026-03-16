import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

sns.set(style="whitegrid")

plt.figure(figsize=(14, 10))

# 1 Histogram - Distribution of Total Bill
plt.subplot(2, 2, 1)
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bill")

# 2 Scatter Plot - Total Bill vs Tip
plt.subplot(2, 2, 2)
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.title("Total Bill vs Tip")

# 3 Box Plot - Total Bill by Day
plt.subplot(2, 2, 3)
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Total Bill by Day")

# 4 Correlation Heatmap
plt.subplot(2, 2, 4)
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# Pairplot (separate visualization)
sns.pairplot(df, hue="sex")
plt.show()
