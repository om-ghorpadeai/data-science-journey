# Day 7 - Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students2.csv")

# Bar chart - Marks of students
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Line chart - Age vs Marks
plt.figure()
plt.plot(df["Age"], df["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()
