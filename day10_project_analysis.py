# Day 10 - Student Performance Analysis Project

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students2.csv")

print("Original Data:\n")
print(df)

# Basic Info
print("\nData Info:\n")
print(df.info())

# Summary statistics
print("\nSummary:\n")
print(df.describe())

# Average marks
avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)

# Top student
top_student = df[df["Marks"] == df["Marks"].max()]
print("\nTop Student:\n", top_student)

# Group by department
print("\nAverage Marks by Department:\n")
print(df.groupby("Department")["Marks"].mean())

# Visualization - Bar plot
plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks of Students")
plt.show()

# Visualization - Box plot
plt.figure()
sns.boxplot(x="Department", y="Marks", data=df)
plt.title("Marks Distribution by Department")
plt.show()
