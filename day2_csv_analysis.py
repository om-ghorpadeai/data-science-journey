# Day 2 - CSV Data Analysis

import pandas as pd

df = pd.read_csv("students.csv")

print("Full Data:\n")
print(df)

print("\nFirst 3 rows:\n")
print(df.head(3))

print("\nColumn Names:")
print(df.columns)

print("\nMarks Column:")
print(df["Marks"])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())
