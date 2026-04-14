# Day 9 - Correlation & Heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students2.csv")

print("Data:\n")
print(df)

# Correlation matrix
corr = df.corr(numeric_only=True)

print("\nCorrelation Matrix:\n")
print(corr)

# Heatmap
plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
