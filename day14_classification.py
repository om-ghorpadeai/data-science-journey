# Day 14 - Classification (Pass/Fail)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load data
df = pd.read_csv("students_classification.csv")

# Features
X = df[["StudyHours", "Marks"]]

# Target
y = df["Result"]

# Model
model = DecisionTreeClassifier()

# Train
model.fit(X, y)

# Predict (StudyHours=3, Marks=55)
prediction = model.predict([[3, 55]])

print("Prediction:", prediction[0])
