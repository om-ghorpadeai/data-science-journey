# Day 6 - Data Cleaning

import pandas as pd

df = pd.read_csv("students_dirty.csv")

print("Original Data:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull())

# Count missing values
print("\nMissing Count:\n")
print(df.isnull().sum())

# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Filling Missing Values:\n")
print(df)
