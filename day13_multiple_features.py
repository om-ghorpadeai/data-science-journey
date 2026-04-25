# Day 13 - Multiple Feature Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("students_ml.csv")

# Features (multiple inputs)
X = df[["Age", "StudyHours"]]

# Target
y = df["Marks"]

# Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict (Age=23, StudyHours=7)
prediction = model.predict([[23, 7]])

print("Predicted Marks:", prediction[0])
