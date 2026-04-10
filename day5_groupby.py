# Day 5 - Grouping Data

import pandas as pd

df = pd.read_csv("students2.csv")

print("Full Data:\n")
print(df)

# Group by Department
print("\nAverage Marks by Department:\n")
print(df.groupby("Department")["Marks"].mean())

# Count students in each department
print("\nNumber of Students per Department:\n")
print(df.groupby("Department")["Name"].count())

# Max marks per department
print("\nHighest Marks in Each Department:\n")
print(df.groupby("Department")["Marks"].max())
