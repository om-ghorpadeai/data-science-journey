# Day 3 - Data Filtering

import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

print("Full Data:\n")
print(df)

# Students with marks greater than 85
print("\nStudents with Marks > 85:\n")
print(df[df["Marks"] > 85])

# Students with age greater than 19
print("\nStudents with Age > 19:\n")
print(df[df["Age"] > 19])

# Students with marks less than 80
print("\nStudents with Marks < 80:\n")
print(df[df["Marks"] < 80])

# Multiple condition
print("\nStudents with Marks > 80 AND Age > 18:\n")
print(df[(df["Marks"] > 80) & (df["Age"] > 18)])

print("\nTop Scorer:")
print(df[df["Marks"] == df["Marks"].max()])
