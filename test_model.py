"""
test_model.py
----------------
Loads the previously saved regression_model.pkl and tests it
with a value entered by the user at runtime.

Run train_model.py first to generate 'regression_model.pkl'.
"""

import pickle
import os
import pandas as pd

MODEL_PATH = "regression_model.pkl"
FEATURE_NAME = "years_experience"
TARGET_NAME = "salary"

# -----------------------------
# 1. Load the saved model
# -----------------------------
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"'{MODEL_PATH}' not found. Please run train_model.py first to create it."
    )

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

print(f"Loaded model from '{MODEL_PATH}'")
print("Model Coefficient (slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

# -----------------------------
# 2. Take runtime input from user and predict
# -----------------------------
while True:
    user_val = input(
        f"\nEnter a value for '{FEATURE_NAME}' to predict {TARGET_NAME} (or type 'exit' to quit): "
    ).strip()

    if user_val.lower() == "exit":
        print("Exiting test script.")
        break

    try:
        val = float(user_val)
        prediction = model.predict(pd.DataFrame([[val]], columns=[FEATURE_NAME]))
        print(f"Predicted {TARGET_NAME} for {FEATURE_NAME}={val}: {prediction[0]:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value (e.g., 4.5) or 'exit'.")
