# Day 11 - Linear Regression (ML)

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("students2.csv")

# Features (input)
X = df[["Age"]]

# Target (output)
y = df["Marks"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for age 22
prediction = model.predict([[22]])

print("Predicted Marks for Age 22:", prediction[0])
