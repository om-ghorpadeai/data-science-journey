# Day 12 - Model Evaluation

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("students2.csv")

# Features and target
X = df[["Age"]]
y = df["Marks"]

# Split data (train + test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predicted:", predictions)
print("Actual:", y_test.values)

# Error
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)
