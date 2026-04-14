# Day 8 - Advanced Visualization with Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv("students2.csv")

# Set style
sns.set()

# Bar plot
plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks of Students (Seaborn)")
plt.show()

# Scatter plot
plt.figure()
sns.scatterplot(x="Age", y="Marks", data=df)
plt.title("Age vs Marks")
plt.show()

# Box plot
plt.figure()
sns.boxplot(x="Department", y="Marks", data=df)
plt.title("Marks Distribution by Department")
plt.show()
