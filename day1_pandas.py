# Day 1 - Pandas Introduction

import pandas as pd

# Creating data
data = {
    "Name": ["Om", "Rahul", "Sneha"],
    "Age": [18, 20, 19],
    "Marks": [85, 90, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:\n")
print(df)
